# RAG-SOTA
RAG using Document Adnotation --> Entity Resolution --> Knowledge Graphs
https://github.com/run-llama/rags




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
        │   ├── annotations_db.py          # Operations related to annotations storage
        │   ├── documents_db.py            # Operations related to documents storage
        │   ├── mongo_client.py            # MongoDB client configuration
        │   └── save_to_db.py              # Handles the database interaction for OCR results and annotations
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
        ├── rag/                           # Retrieval-Augmented Generation module
        │   ├── __init__.py
        │   ├── document_retriever.py      # Handles retrieval of documents based on queries
        │   ├── answer_generator.py        # Generates answers from retrieved documents and annotations
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
        ├── ner/                           
        │   ├── __init__.py
        │   ├── ner_model.py               # NER model implementation
        │   └── ner_utils.py               # Utilities for NER tasks
        │
        ├── knowledge_graph/               
        │   ├── __init__.py
        │   ├── graph_builder.py           # Script for building knowledge graphs
        │   └── graph_utils.py             # Utilities for graph operations
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
            
            For MongoDB Compass (GUI, like PgAdmin)
            /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
            brew install --cask mongodb-compass
            connect to mongodb://localhost:27017




## RAG MODEL

Tydpe of implementation will be "Hybrid Fusion"


## Knowledge Graph

https://siwei.io/en/demos/text2cypher/
https://colab.research.google.com/drive/1tLjOg2ZQuIClfuWrAC2LdiZHCov8oUbs?usp=sharing#scrollTo=3g6agniJOudp

## Key KG related components

- [KnowledgeGraphIndex](https://gpt-index.readthedocs.io/en/stable/examples/index_structs/knowledge_graph/KnowledgeGraphDemo.html) is an Index to:
  - Indexing stage:
    - Extract data into KG with LLM or any other callable models
    - Persist KG data into `storeage_context.graph_store`
  - Querying stage:
    - `as_query_engine()` to enable 0-shot Graph RAG
    - `as_retriever()` to create an advanced Graph involving RAG
- [KnowledgeGraphRAGRetriever](https://gpt-index.readthedocs.io/en/stable/examples/query_engine/knowledge_graph_rag_query_engine.html)
  - Instanctiate:
    - Create a `storeage_context.graph_store` as the init argument.
  - Querying stage:
    - pass to `RetrieverQueryEngine` to become a Graph RAG query engine on any existing KG
    - combined with other RAG pipeline

- [KnowledgeGraphQueryEngine](https://gpt-index.readthedocs.io/en/stable/examples/query_engine/knowledge_graph_query_engine.html), Text2Cypher Query engine
  - Instanctiate:
    - Create a `storeage_context.graph_store` as the init argument.
  - Querying stage:
    - Text2cypher to get answers towards the KG in graph_store.
    - Optionally, `generate_query()` only compose a cypher query.


     https://gpt-index.readthedocs.io/en/stable/examples/index_structs/knowledge_graph/KnowledgeGraphIndex_vs_VectorStoreIndex_vs_CustomIndex_combined.html

