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


Llama Index

https://llamahub.ai/l/readers/llama-index-readers-nougat-ocr?from=



PDF Parser Project Structure

pdf_parser_project/
│
├── src/                    # Source code for the PDF parser
│   ├── __init__.py         # Makes src a Python package
│   ├── main.py             # Entry point to run the parser
│   ├── pdf_parser.py       # Core functionalities for PDF parsing
│   └── ocr.py              # OCR functionalities for image-based PDFs
│
├── tests/                  # Unit tests for your application
│   ├── __init__.py         # Makes tests a Python package
│   └── test_pdf_parser.py  # Test cases for pdf_parser functionalities
│
├── docs/                   # Documentation files
│   └── README.md           # Project README with usage instructions
│
├── data/                   # Folder for PDF files and other data
│   ├── input/              # Input PDFs to be parsed
│   └── output/             # Output from the parsing process
│
├── requirements.txt        # Project dependencies
└── .gitignore              # Specifies intentionally untracked files to ignore

