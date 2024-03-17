# RAG-SOTA/interface/streamlit_app.py
import sys
from pathlib import Path

project_root = Path(__file__).parent.parent.absolute()
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

print(project_root)


import streamlit as st
from pymongo import MongoClient
from typing import List
from pdf_parser import parse_documents_from_path_with_llama_index


from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.core import VectorStoreIndex
from llama_index.core import StorageContext
from llama_index.core import Response
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import Settings
from llama_index.core import SimpleDirectoryReader
from llama_parse import LlamaParse
Settings.embed_model = OpenAIEmbedding()


import os
from dotenv import load_dotenv
load_dotenv()
LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")
OPENAI_API_KEY =  os.getenv("OPENAI_API_KEY")


from llama_index.llms.openai import OpenAI

embed_model=OpenAIEmbedding(model="text-embedding-3-small")
llm = OpenAI(model="gpt-3.5-turbo-0125")

Settings.llm = llm
Settings.embed_model = embed_model






"""
def get_db():
    client = MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as per your MongoDB setup
    db = client["ocr_documents_db"] 
    return db
"""

def get_vector_storage():
    client = MongoClient("mongodb://localhost:27017/")  # Adjust the connection string as per your MongoDB setup
    embeding_db = client["embedings_db"]  
    v_store = MongoDBAtlasVectorSearch(embeding_db)
    vector_storage_context = StorageContext.from_defaults(vector_store=v_store)
    return v_store, vector_storage_context


# https://docs.llamaindex.ai/en/latest/examples/vector_stores/MongoDBAtlasVectorSearch.html
# https://docs.llamaindex.ai/en/stable/module_guides/models/embeddings.html


from llama_index.core.node_parser import SimpleNodeParser
node_parser = SimpleNodeParser()
nodes = node_parser.get_nodes_from_documents(documents)



from pathlib import Path

def upload_and_process_documents():
    # Initiate file upload through the UI
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True,
                                      type=['pdf', 'docx', 'png', 'jpg', 'jpeg', 'txt', 'md', 'ipynb', 'csv', 'pptx', 'mp3', 'mp4'])
    docs = []
    if uploaded_files:
        # Define and ensure the directory for saving uploaded files exists
        uploads_dir = Path.cwd() / "uploaded_files"
        uploads_dir.mkdir(exist_ok=True)
        
        # Save uploaded files to the specified directory
        for uploaded_file in uploaded_files:
            file_path = uploads_dir / uploaded_file.name
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
        
        # Setup the parser with an API key and the desired result type
        parser = LlamaParse(api_key="LLAMA_CLOUD_API_KEY", result_type="markdown")
        file_extractor = {".pdf": parser}
        
        # Process the saved files using the specified parser
        reader = SimpleDirectoryReader(uploads_dir, file_extractor=file_extractor)
        docs = reader.load_data()
        
        # Notify the user of success
        st.success("Files processed and saved successfully.")
    
    return docs



def enter_query():
    query = st.text_input("Enter your query here:")
    return query

def process_query(query: str) -> str:
    """
    Processes a query against the document base and generates a response.
    
    :param query: The user's query as a string.
    :return: A string containing the generated answer.
    """
    response = vector_index.as_query_engine().query(enter_query())
    return response


def display_response(response):
    st.write((Markdown(f"<b>{response}</b>")))



"""
##### Get a ref_doc_id used for response
typed_response = (
    response if isinstance(response, Response) else response.get_response()
)
ref_doc_id = typed_response.source_nodes[0].node.ref_doc_id
print(v_store._collection.count_documents({"metadata.ref_doc_id": ref_doc_id}))

####
"""

"""
# Test store delete
if ref_doc_id:
    v_store.delete(ref_doc_id)
    print(v_store._collection.count_documents({}))
)
"""

def main():

    st.title("RAG-SOTA Document Query Application")
    docs = upload_and_process_documents()
    v_store, vector_storage_context = get_vector_storage()
    vector_index = VectorStoreIndex.from_documents( docs, storage_context= vector_storage_context, embed_model=embed_model)

    print("number of docs in vector index after upload is:")
    print(v_store._collection.count_documents({}))

    query = enter_query()
    if query:
        response = process_query(query)
        display_response(response)




if __name__ == "__main__":
    main()



### end ###
