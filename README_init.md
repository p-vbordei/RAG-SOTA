# RAG-SOTA Project Documentation

## Overview
RAG-SOTA (Retrieval-Augmented Generation - State Of The Art) is a evolving project aimed at developing a cutting-edge document processing and query answering system. It utilizes advanced NLP techniques for efficient information retrieval, document annotation, and generating coherent responses to user queries. Designed for scalability, it caters to SMEs with a focus on simplicity, efficiency, and secure handling of proprietary data.

## Development Environment
Developed and tested on MacBook Pro with M1 chip, utilizing Docker for containerization, MongoDB for database management, and Streamlit for web interface development.

## Installation & Getting Started

1. **MongoDB Setup**: Install MongoDB locally or via Docker. Ensure the MongoDB service is running.
   ```bash
   brew tap mongodb/brew
   brew install mongodb-community@5.0
   brew services start mongodb/brew/mongodb-community

RAG using Document Annotation
https://github.com/run-llama/rags

### Knowledge Base for the project
RAG Architecture
https://www.artiquare.com/anatomy-of-advanced-rag-systems/

Choosing the embedding model
https://medium.com/barnacle-labs/embeddings-in-production-or-how-nothing-scales-like-youd-expect-it-to-part-1-costs-to-embed-a82482765215

Limited information volume (up to one thousand documents for initial project scope) --> 1k documents x 50 pages = 50k x 1000 tokens / page = ~50M Tokens / year for embedding purposes. Also estimating a chunk size of 1000k Tokens it also means 50k Chunks.
--> Embedding can be via API

### Existing RAG Implementations
https://replit.com/@taranjeetio/Embedchain-Chat-Bot#README.md
https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/agent/multi_document_agents.ipynb#scrollTo=d476c54b-98af-4d2a-8f17-4baa37d0d360

### Business Objective
- Be able to implement at SME Level
- Proprietary data considerations and safeguards
- Simple-Stupid ease of use, minimize the number of buttons.
- Development Approach
- Validate First
- Simplified Design
- POC / Minimum Number of Features
- Enhance in Iteration 2

### Minimum Number of Features
- A user can upload a PDF or a Word document somewhere.
- A user can upload somewhere other 10 documents from the same project.
- A user can use an interface to ask questions regarding the documentation and receive accurate responses.
- Features Not to be implemented in iteration 1
- History of discussions
- Nice looking interface

### Interfaces under consideration for MVP
- Streamlit
- Retool

## Pdf Parser
### KNOWLEDGE SOURCE

https://pradeepundefned.medium.com/a-comparison-of-python-libraries-for-pdf-data-extraction-for-text-images-and-tables-c75e5dbcfef8
https://www.researchgate.net/publication/369368936_A_Benchmark_of_PDF_Information_Extraction_Tools_using_a_Multi-Task_and_Multi-Domain_Evaluation_Framework_for_Academic_Documents
https://huggingface.co/spaces/ABBNikit/pdf-chatbot/blob/main/app.py
https://huggingface.co/spaces/saifmaxx/pdf_m/blob/main/app.py

### Llama Index
https://llamahub.ai/l/readers/llama-index-readers-nougat-ocr?from=

### Install Tesseract


        For macOS 
        brew install tesseract
        brew install tesseract-lang

        For Ubuntu
        sudo apt-get update
        sudo apt-get install tesseract-ocr

        brew install git-lfs
        git lfs install


### Project Structure

    RAG-SOTA/
    │── pdf_parser.py          # PDF parsing implementation
    ├── streamlit_app.py           # Streamlit application for MVP
    ├── uploaded_files/             # project files for upload / parsing             
    ├── requirements.txt               # Main project dependencies
    └── .gitignore

### Development Environment
MacBook Pro, M1 (Apple Silicon)
VS Code
Docker available


### DB
Install Locally:

        brew tap mongodb/brew
        brew install mongodb-community@5.0

Run mongo

        Start & Stop
        brew services start mongodb/brew/mongodb-community
        brew services stop mongodb/brew/mongodb-community

        Test Install
        mongosh

Install with Docker:

        docker pull mongo
        docker run --name mongodb -d -p 27017:27017 mongo:latest
        docker exec -it mongodb mongosh


For MongoDB Compass (GUI, like PgAdmin)

        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        brew install --cask mongodb-compass
        connect to mongodb://localhost:27017

In order to run Streamlit

        streamlit run streamlit_app.py


### pip install pipreqs

        pipreqs /Users/vladbordei/Documents/Development/RAG-SOTA


### create env

        conda create --name rag python=3.10
        conda activate rag
        pip install -r requirements.txt


### clear cache

        sudo find / -type d -name "__pycache__" -exec rm -r {} +
        pip cache purge
