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
