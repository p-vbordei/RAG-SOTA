# RAG-SOTA
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
    ├── db/  
    │   ├── __init__.py
    │   ├── documents_db.py            # Operations related to documents storage
    │   ├── mongo_client.py            # MongoDB client configuration
    │   └── save_to_db.py              # Handles the database interaction for OCR results
    │
    ├── embedding/                     
    │   ├── __init__.py
    │   ├── api_client.py              # API client for external embedding services
    │   └── embedding_utils.py         # Utilities for generating and managing document embeddings
    │
    ├── indexing/                      
    │   ├── __init__.py
    │   ├── vector_store.py            # Handles creation and management of vector store indexes
    │   └── semantic_search.py         # Implements semantic search capabilities
    │
    ├── rag/                           
    │   ├── __init__.py
    │   ├── document_retriever.py      # Handles retrieval of documents based on queries
    │   ├── answer_generator.py        # Generates answers from retrieved documents
    │   └── rag_utils.py               # Utilities for RAG operations, including document scoring and ranking
    │
    ├── agents/                        
    │   ├── __init__.py
    │   ├── document_agent.py          # Implementation of document-specific agents
    │   └── top_level_agent.py         # Implementation of the top-level orchestrating agent
    │
    ├── summarization/                 
    │   ├── __init__.py
    │   ├── summary_generator.py       # Script for generating document summaries
    │   └── summary_index.py           # Handles indexing and retrieval of document summaries
    │
    ├── pdf_parser/                    
    │   ├── src/
    │   │   ├── __init__.py
    │   │   ├── pdf_parser_main.py     # Main script for PDF parsing
    │   │   ├── pdf_parser.py          # PDF parsing implementation
    │   │   └── ocr.py                 # OCR functionality
    │   ├── tests/
    │   │   ├── __init__.py
    │   │   └── test_pdf_parser.py     # Tests for PDF parser
    │   ├── data/
    │   │   ├── input/
    │   │   └── output/
    │   ├── requirements.txt
    │   └── .gitignore
    │
    ├── interface/                     
    │   ├── __init__.py
    │   ├── streamlit_app.py           # Streamlit application for MVP
    │   └── retool_integration.py      # Optional: Integration with Retool if needed
    │
    ├── tests/                         
    │   ├── __init__.py
    │   └── test_end_to_end.py         # End-to-end tests of the pipeline
    │
    ├── docs/                          
    │   ├── setup.md
    │   ├── usage.md 
    │   └── development.md
    │
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

bash
        Start & Stop
        brew services start mongodb/brew/mongodb-community
        brew services stop mongodb/brew/mongodb-community

        Test Install
        mongosh
Install with Docker:
docker pull mongo
docker run --name mongodb -d -p 27017:27017 mongo:latest
docker exec -it mongodb mongosh

bash
        For MongoDB Compass (GUI, like PgAdmin)
        /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
        brew install --cask mongodb-compass
        connect to mongodb://localhost:27017


### RAG MODEL
Type of implementation will be "Hybrid Fusion"

