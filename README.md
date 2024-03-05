# RAG-SOTA
RAG using Document Adnotation --> Entity Resolution --> Knowledge Graphs




## Knowledge Base for the project

RAG Architecture
https://www.artiquare.com/anatomy-of-advanced-rag-systems/


Choosing the embdeding model
https://medium.com/barnacle-labs/embeddings-in-production-or-how-nothing-scales-like-youd-expect-it-to-part-1-costs-to-embed-a82482765215
Limited information volume (up to one thousand documents for initial project scope) --> 1k documents x 50 pages = 50k x 1000 tokens / page = ~50M Tokens / year for embeding purposes. Also estimating a chunk size of 1000k Tokens it also means 50k Chunks.
--> Embeding can be via API

Existing RAG Implementations
https://replit.com/@taranjeetio/Embedchain-Chat-Bot#README.md
https://colab.research.google.com/github/run-llama/llama_index/blob/main/docs/examples/agent/multi_document_agents.ipynb#scrollTo=d476c54b-98af-4d2a-8f17-4baa37d0d360

Choosing NER Algorithm
https://huggingface.co/tomaarsen/span-marker-mbert-base-multinerd
or
SpaCy



## Business Objective
- Be able to implement at SME Level
- Proprietary data considerations and safeguards
- Simple-Stupid ease of use, minimize number of buttons.

## Development Approach
- Validate First
- Simplified Design
- POC / Minimum Number of Features
- Enhace in Interation 2

## Minimum Number of Features
- A user can upload somewhere a pdf or a word
- A user can upload somewhere other 10 docuemnts from the same project
- A user can use a interface to ask questions regarding the documentation and receive accurate responses

## Features Not to be implemented in iteration 1
- History of discussions
- Nice looking interface


## Interfaces under consideration for MVP
- Streamlit
- Retool


## Pdf Parser
KNOWLEDGE SOURCE

https://pradeepundefned.medium.com/a-comparison-of-python-libraries-for-pdf-data-extraction-for-text-images-and-tables-c75e5dbcfef8
https://www.researchgate.net/publication/369368936_A_Benchmark_of_PDF_Information_Extraction_Tools_using_a_Multi-Task_and_Multi-Domain_Evaluation_Framework_for_Academic_Documents
https://huggingface.co/spaces/ABBNikit/pdf-chatbot/blob/main/app.py
https://huggingface.co/spaces/saifmaxx/pdf_m/blob/main/app.py


Llama Index
https://llamahub.ai/l/readers/llama-index-readers-nougat-ocr?from=



 ## Kindly install tessaract
            For macOS 
            brew install tesseract
            brew install tesseract-lang

            For Ubuntu
            sudo apt-get update
            sudo apt-get install tesseract-ocr



            brew install git-lfs
            git lfs install



## NER Model
This project needs to handle multiple european languages, especially Romanian. It is a critical project condition, to be able to be performant in Romanian.
Initial library:
https://huggingface.co/tomaarsen/span-marker-mbert-base-multinerd
tomaarsen/span-marker-mbert-base-multinerd





## Project Structure

            RAG-SOTA/
            ├── db/  
            │   ├── __init__.py
            │   ├── annotations_db.py     # Operations related to annotations storage
            │   ├── documents_db.py       # Operations related to documents storage
            │   └── mongo_client.py       # MongoDB client configuration
            │   ├── save_to_db.py #  that handles the database interaction for OCR

            ├── embedding/                # Module for document embedding
            │   ├── __init__.py
            │   └── api_client.py        # API client for external embedding services
            │
            ├── ner/                      # Named Entity Recognition (NER) module
            │   ├── __init__.py
            │   ├── ner_model.py         # NER model implementation
            │   └── ner_utils.py         # Utilities for NER tasks
            │
            ├── knowledge_graph/         # Knowledge graph construction module
            │   ├── __init__.py
            │   ├── graph_builder.py     # Script for building knowledge graphs
            │   └── graph_utils.py       # Utilities for graph operations
            │
            ├── pdf_parser/               # PDF parsing module (as specified)
            │   ├── src/
            │   │   ├── __init__.py
            │   │   ├── main.py     # Main script for PDF parsing
            │   │   ├── pdf_parser.py # PDF parsing implementation
            │   │   └── ocr.py # OCR functionality
            │   ├── tests/
            │   │   ├── __init__.py
            │   │   └── test_pdf_parser.py  # Tests for PDF parser
            │   ├── docs/
            │   │   └── README.md
            │   ├── data/
            │   │   ├── input/
            │   │   └── output/
            │   ├── requirements.txt
            │   └── .gitignore
            │
            ├── interface/               # User interface module
            │   ├── __init__.py
            │   ├── streamlit_app.py     # Streamlit application for MVP
            │   └── retool_integration.py # Optional: Integration with Retool if needed
            │
            ├── tests/                   # Integration and unit tests for the project
            │   ├── __init__.py
            │   └── test_end_to_end.py   # End-to-end tests of the pipeline
            │
            ├── docs/                    # Project documentation
            │   ├── setup.md
            │   ├── usage.md 
            │   └── development.md
            │
            ├── requirements.txt         # Main project dependencies
            └── .gitignore




## Develpoment Environment
- Macbook Pro, M1 (Apple Silicone)
- VS Code
- Docker available


## DB
Install Locally:
            brew tap mongodb/brew
            brew install mongodb-community@5.0

            Start& Stop
            brew services start mongodb/brew/mongodb-community
            brew services stop mongodb/brew/mongodb-community

            Test Install
            mongosh

Install with Docker:
            docker pull mongo
            docker run --name mongodb -d -p 27017:27017 mongo:latest
            docker exec -it mongodb mongosh


