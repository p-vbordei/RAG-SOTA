import os
import shutil
import streamlit as st
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.vectorstores import FAISS
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnablePassthrough
from langchain_community.llms import Together
from langchain_community.document_loaders import UnstructuredPDFLoader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings import HuggingFaceEmbeddings

os.environ["TOGETHER_API_KEY"] =os.getenv("TOGETHER_API_KEY")


def inference(chain, input_query):
    """Invoke the processing chain with the input query."""
    result = chain.invoke(input_query)
    return result


def create_chain(retriever, prompt, model):
    """Compose the processing chain with the specified components."""
    chain = (
        {"context": retriever, "question": RunnablePassthrough()}
        | prompt
        | model
        | StrOutputParser()
    )
    return chain


def generate_prompt():
    """Define the prompt template for question answering."""
    template = """<s>[INST] Answer the question in a simple sentence based only on the following context:
                  {context}
                  Question: {question} [/INST] 
               """
    return ChatPromptTemplate.from_template(template)


def configure_model():
    """Configure the language model with specified parameters."""
    return Together(
        model="mistralai/Mixtral-8x7B-Instruct-v0.1",
        temperature=0.1,
        max_tokens=3000,
        top_k=50,
        top_p=0.7,
        repetition_penalty=1.1,
    )


def configure_retriever(pdf_loader):
    """Configure the retriever with embeddings and a FAISS vector store."""
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector_db = FAISS.from_documents(pdf_loader, embeddings)
    return vector_db.as_retriever()


def load_documents(path):
    """Load and preprocess documents from PDF files located at the specified path."""
    pdf_loader = []
    for file in os.listdir(path):
        if file.endswith('.pdf'):
            filepath = os.path.join(path, file)
            loader = UnstructuredPDFLoader(filepath)
            documents = loader.load()
            text_splitter = CharacterTextSplitter(chunk_size=18000, chunk_overlap=10)
            docs = text_splitter.split_documents(documents)
            pdf_loader.extend(docs)
    return pdf_loader


def process_document(path, input_query):
    """Process the document by setting up the chain and invoking it with the input query."""
    pdf_loader = load_documents(path)
    llm_model = configure_model()
    prompt = generate_prompt()
    retriever = configure_retriever(pdf_loader)
    chain = create_chain(retriever, prompt, llm_model)
    response = inference(chain, input_query)
    return response


def main():
    """Main function to run the Streamlit app."""
    tmp_folder = '/tmp/1'
    os.makedirs(tmp_folder,exist_ok=True)

    st.title("Document Q&A Chatbot")

    uploaded_files = st.sidebar.file_uploader("Choose PDF files", accept_multiple_files=True, type='pdf')
    if uploaded_files:
        for file in uploaded_files:
            with open(os.path.join(tmp_folder, file.name), 'wb') as f:
                f.write(file.getbuffer())
        st.success('File successfully uploaded. Start prompting!')
    if 'chat_history' not in st.session_state:
        st.session_state.chat_history = []

    if uploaded_files:
        with st.form(key='question_form'):
            user_query = st.text_input("Ask a question:", key="query_input")
            if st.form_submit_button("Ask") and user_query:
                response = process_document(tmp_folder, user_query)
                st.session_state.chat_history.append({"question": user_query, "answer": response})
            
        if st.button("Clear Chat History"):
            st.session_state.chat_history = []
        for chat in st.session_state.chat_history:
            st.markdown(f"**Q:** {chat['question']}")
            st.markdown(f"**A:** {chat['answer']}")
            st.markdown("---")
    else:
        st.success('Upload Document to Start Process !')

    if st.sidebar.button("REMOVE UPLOADED FILES"):
        document_count = os.listdir(tmp_folder)
        if len(document_count) > 0:
            shutil.rmtree(tmp_folder)
            st.sidebar.write("FILES DELETED SUCCESSFULLY !!!")
        else:
            st.sidebar.write("NO DOCUMENT FOUND TO DELETE !!! PLEASE UPLOAD DOCUMENTS TO START PROCESS !! ")


if __name__ == "__main__":
    main()