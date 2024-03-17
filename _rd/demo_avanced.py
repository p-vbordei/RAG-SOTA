# %% [markdown]
# # Llama Parser <> LlamaIndex
# 
# This notebook is a complete walkthrough for using `LlamaParse` for RAG applications with `LlamaIndex`.
# 
# Note for this example, we are using the `llama_index >=0.10.4` version

# %%
!pip install llama-index
!pip install llama-index-core
!pip install llama-index-embeddings-openai
!pip install llama-index-postprocessor-flag-embedding-reranker
!pip install git+https://github.com/FlagOpen/FlagEmbedding.git
!pip install llama-parse

# %%
!wget 'https://raw.githubusercontent.com/run-llama/llama_index/main/docs/examples/data/10q/uber_10q_march_2022.pdf' -O './uber_10q_march_2022.pdf'

# %% [markdown]
# Some OpenAI and LlamaParse details

# %%
# llama-parse is async-first, running the async code in a notebook requires the use of nest_asyncio
import nest_asyncio
nest_asyncio.apply()

import os
# API access to llama-cloud
os.environ["LLAMA_CLOUD_API_KEY"] = "llx-"

# Using OpenAI API for embeddings/llms
os.environ["OPENAI_API_KEY"] = "sk-"

# %%
from llama_index.llms.openai import OpenAI
from llama_index.embeddings.openai import OpenAIEmbedding
from llama_index.core import VectorStoreIndex
from llama_index.core import Settings

embed_model=OpenAIEmbedding(model="text-embedding-3-small")
llm = OpenAI(model="gpt-3.5-turbo-0125")

Settings.llm = llm
Settings.embed_model = embed_model


# %% [markdown]
# ## Using brand new `LlamaParse` PDF reader for PDF Parsing
# 
# we also compare two different retrieval/query engine strategies:
# 1. Using raw Markdown text as nodes for building index and apply simple query engine for generating the results;
# 2. Using `MarkdownElementNodeParser` for parsing the `LlamaParse` output Markdown results and building recursive retriever query engine for generation.

# %%
from llama_parse import LlamaParse

documents = LlamaParse(result_type="markdown").load_data('./uber_10q_march_2022.pdf')

# %%
print(documents[0].text[:1000] + '...')

# %%
from llama_index.core.node_parser import MarkdownElementNodeParser

node_parser = MarkdownElementNodeParser(llm=OpenAI(model="gpt-3.5-turbo-0125"), num_workers=8)

# %%
nodes = node_parser.get_nodes_from_documents(documents)

# %%
base_nodes, objects = node_parser.get_nodes_and_objects(nodes)

# %%
recursive_index = VectorStoreIndex(nodes=base_nodes+objects)
raw_index = VectorStoreIndex.from_documents(documents)

# %%
from llama_index.postprocessor.flag_embedding_reranker import FlagEmbeddingReranker

reranker = FlagEmbeddingReranker(
    top_n=5,
    model="BAAI/bge-reranker-large",
)

recursive_query_engine = recursive_index.as_query_engine(
    similarity_top_k=15, 
    node_postprocessors=[reranker], 
    verbose=True
)

raw_query_engine = raw_index.as_query_engine(similarity_top_k=15, node_postprocessors=[reranker])

# %%
print(len(nodes))

# %% [markdown]
# ## Using `new LlamaParse` as pdf data parsing methods and retrieve tables with two different methods
# we compare base query engine vs recursive query engine with tables

# %% [markdown]
# ### Table Query Task: Queries for Table Question Answering

# %%
query = "how is the Cash paid for Income taxes, net of refunds from Supplemental disclosures of cash flow information?"

response_1 = raw_query_engine.query(query)
print("\n***********New LlamaParse+ Basic Query Engine***********")
print(response_1)

response_2 = recursive_query_engine.query(query)
print("\n***********New LlamaParse+ Recursive Retriever Query Engine***********")
print(response_2)


# %% [markdown]
# ![image.png](attachment:image.png)

# %%
query = "what is the change of free cash flow and what is the rate from the financial and operational highlights?"

response_1 = raw_query_engine.query(query)
print("\n***********New LlamaParse+ Basic Query Engine***********")
print(response_1)

response_2 = recursive_query_engine.query(query)
print("\n***********New LlamaParse+ Recursive Retriever Query Engine***********")
print(response_2)

# %% [markdown]
# ![image.png](attachment:image.png)

# %%
query = "what is the net loss value attributable to Uber compared to last year?"

response_1 = raw_query_engine.query(query)
print("\n***********New LlamaParse+ Basic Query Engine***********")
print(response_1)

response_2 = recursive_query_engine.query(query)
print("\n***********New LlamaParse+ Recursive Retriever Query Engine***********")
print(response_2)

# %% [markdown]
# ![image.png](attachment:image.png)

# %%
query = "What were cash flows like from investing activities?"

response_1 = raw_query_engine.query(query)
print("\n***********New LlamaParse+ Basic Query Engine***********")
print(response_1)

response_2 = recursive_query_engine.query(query)
print("\n***********New LlamaParse+ Recursive Retriever Query Engine***********")
print(response_2)

# %% [markdown]
# ![image.png](attachment:image.png)


