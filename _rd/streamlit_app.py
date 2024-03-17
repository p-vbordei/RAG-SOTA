# RAG-SOTA/interface/streamlit_app.py
import sys
from pathlib import Path

# Get the absolute path of the project root (RAG-SOTA directory)
project_root = Path(__file__).parent.parent.absolute()

# Add the project root to the Python path
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

#print("sys append")
#print(sys.path)
print(project_root)


import streamlit as st
from typing import List


from pdf_parser import parse_documents_from_path_with_llama_index
from pymongo import MongoClient



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


import nest_asyncio
nest_asyncio.apply()

import os
from dotenv import load_dotenv
load_dotenv()
LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")


from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings

embed_model=OpenAIEmbedding(model="text-embedding-3-small")
llm = OpenAI(model="gpt-3.5-turbo-0125")

Settings.llm = llm
Settings.embed_model = embed_model


"""
from llama_parse import LlamaParse  # pip install llama-parse

parser = LlamaParse(
    api_key=LLAMA_CLOUD_API_KEY,  # can also be set in your env as LLAMA_CLOUD_API_KEY
    result_type="markdown"  # "markdown" and "text" are available
)
file_extractor = {".pdf": parser}
reader = SimpleDirectoryReader("./data", file_extractor=file_extractor)
documents = reader.load_data()

"""


def get_db():
    client = MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as per your MongoDB setup
    db = client["ocr_documents_db"] 
    return db

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




def process_and_save_documents(uploaded_files):
    uploads_dir = Path.cwd() / "uploaded_files"
    uploads_dir.mkdir(exist_ok=True)

    for uploaded_file in uploaded_files:
        file_path = uploads_dir / uploaded_file.name
        with open(file_path, "wb") as f:
            f.write(uploaded_file.getbuffer())
        
        documents_contents = parse_documents_from_path_with_llama_index(str(file_path))
        text = "\n".join(documents_contents) if documents_contents else None
        
        # Save to database (pseudo code, implement according to your schema)
        db = get_db()
        db.documents.insert_one({"filename": uploaded_file.name, "content": text})


def upload_documents():
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True,
                                      type=['pdf', 'docx', 'png', 'jpg', 'jpeg', 'txt', 'md', 'ipynb', 'csv', 'pptx', 'mp3', 'mp4'])
    if uploaded_files:
        # Define the directory to save uploaded files, e.g., under "uploaded_files" within the project root.
        uploads_dir = project_root / "uploaded_files"
        uploads_dir.mkdir(exist_ok=True)  # Create the directory if it doesn't exist.

    if uploaded_files:
        process_and_save_documents(uploaded_files)
        st.success("Files processed and saved successfully.")


def enter_query():
    query = st.text_input("Enter your query here:")
    return query

def process_query(query: str) -> str:
    """
    Processes a query against the document base and generates a response.
    
    :param query: The user's query as a string.
    :return: A string containing the generated answer.
    """
    # Retrieve relevant documents based on the query
    document_ids = retrieve_documents(query, top_k=5)  # Assume this function returns a list of document IDs
    
    # Fetch document details for the retrieved document IDs
    documents = [fetch_document_details(doc_id) for doc_id in document_ids]
    
    # Generate an answer based on the retrieved documents
    answer = generate_answer(documents, query)
    
    return answer


def display_response(response):
    st.write(response)

def main():
    st.title("RAG-SOTA Document Query Application")
    upload_documents()
    query = enter_query()
    if query:
        response = process_query(query)
        display_response(response)

if __name__ == "__main__":
    main()



### end ###
