# RAG-SOTA/indexing/vector_store.py
import numpy as np
from pymongo import MongoClient

from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.core import Response
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
Settings.embed_model = OpenAIEmbedding()



def get_vector_storage():
    client = MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as per your MongoDB setup
    embeding_db = client["embedings_db"]  
    v_store = MongoDBAtlasVectorSearch(embeding_db)
    vector_storage_context = StorageContext.from_defaults(vector_store=v_store)
    return v_store, vector_storage_context


# https://docs.llamaindex.ai/en/latest/examples/vector_stores/MongoDBAtlasVectorSearch.html
# https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings.html


v_store, vector_storage_context = get_vector_storage()
vector_index = VectorStoreIndex.from_documents( docs, storage_context= vector_storage_context, embed_model=embed_model)

print("number of docs in vector index is:")
print(v_store._collection.count_documents({}))


### Get a Response
response = vector_index.as_query_engine().query("What was Uber's revenue?")
display(Markdown(f"<b>{response}</b>"))



##### Get a ref_doc_id used for response
typed_response = (
    response if isinstance(response, Response) else response.get_response()
)
ref_doc_id = typed_response.source_nodes[0].node.ref_doc_id
print(v_store._collection.count_documents({"metadata.ref_doc_id": ref_doc_id}))

####


"""
# Test store delete
if ref_doc_id:
    v_store.delete(ref_doc_id)
    print(v_store._collection.count_documents({}))
)
"""


