# RAG-SOTA/interface/streamlit_app.py
import os
import sys
from pathlib import Path
from dotenv import load_dotenv
import streamlit as st

# Load environment variables
load_dotenv()
LLAMA_CLOUD_API_KEY = os.getenv("LLAMA_CLOUD_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")

# Ensure project root is in sys.path
project_root = Path(__file__).parent.parent.absolute()
if str(project_root) not in sys.path:
    sys.path.append(str(project_root))

# Import after adding project root to sys.path if necessary
from pymongo import MongoClient
from llama_index.vector_stores.mongodb import MongoDBAtlasVectorSearch
from llama_index.core import VectorStoreIndex, StorageContext, SimpleDirectoryReader, Settings
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.llms.openai import OpenAI
from llama_parse import LlamaParse

# Configure LlamaIndex settings
Settings.embed_model = OpenAIEmbedding(model="text-embedding-3-small")
Settings.llm = OpenAI(model="gpt-3.5-turbo-0125")

def get_vector_storage():
    client = MongoClient("mongodb://localhost:27017/")
    embedding_db = client["embeddings_db"]
    v_store = MongoDBAtlasVectorSearch(embedding_db)
    vector_storage_context = StorageContext.from_defaults(vector_store=v_store)
    return v_store, vector_storage_context

def upload_and_process_documents():
    uploaded_files = st.file_uploader("Choose files", accept_multiple_files=True,
                                      type=['pdf', 'docx', 'png', 'jpg', 'jpeg', 'txt', 'md', 'ipynb', 'csv', 'pptx', 'mp3', 'mp4'])
    docs = []
    if uploaded_files:
        uploads_dir = Path.cwd() / "uploaded_files"
        uploads_dir.mkdir(exist_ok=True)
        
        for uploaded_file in uploaded_files:
            file_path = uploads_dir / uploaded_file.name
            with open(file_path, "wb") as f:
                f.write(uploaded_file.getbuffer())
        
        parser = LlamaParse(api_key=LLAMA_CLOUD_API_KEY, result_type="markdown")
        file_extractor = {".pdf": parser}
        
        reader = SimpleDirectoryReader(uploads_dir, file_extractor=file_extractor)
        docs = reader.load_data()
        
        st.success("Files processed and saved successfully.")
    
    return docs

def enter_query():
    query = st.text_input("Enter your query here:")
    return query

def process_query(query, vector_index):
    response = vector_index.as_query_engine().query(query)
    return response

def display_response(response):
    st.markdown(f"<b>{response}</b>", unsafe_allow_html=True)

def main():
    st.title("RAG-SOTA Document Query Application")
    docs = upload_and_process_documents()
    
    if docs:
        v_store, vector_storage_context = get_vector_storage()
        vector_index = VectorStoreIndex.from_documents(docs, storage_context=vector_storage_context, embed_model=Settings.embed_model)
        
        query = enter_query()
        if query:
            response = process_query(query, vector_index)
            display_response(response)

if __name__ == "__main__":
    main()



### end ###
