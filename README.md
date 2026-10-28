# EdTech FAQ Bot

A Streamlit Q&A bot that answers questions about an online course platform from its FAQ file.

## Why this exists
Practice with retrieval-augmented generation (RAG) on a real FAQ dataset (Codebasics), so answers come from the platform's own text.

## What it does
- Loads `codebasics_faqs.csv` and embeds each entry with BGE embeddings
- Saves the vectors to a local FAISS index ("Create Knowledgebase" button)
- Finds the closest FAQ entries for a question and answers with GPT-4 through a `RetrievalQA` chain
- `project1.ipynb` shows the same steps one by one

## Project structure
```
query_bot_edtech/
├── faiss_index/         Saved FAISS vector index
├── codebasics_faqs.csv  FAQ questions and answers
├── langchain_helper.py  Index building and QA chain
├── main.py              Streamlit app
├── project1.ipynb       Step-by-step notebook
├── requirements.txt     Python dependencies
└── projectenv/          Local virtual environment
```

## Getting started
Requirements: Python 3.10+, an OpenAI API key.
```bash
git clone https://github.com/abhijha8287/query_bot_edtech.git
cd query_bot_edtech
python -m venv .venv && source .venv/bin/activate
pip install -r requirements.txt sentence-transformers
mkdir -p .streamlit && echo 'api_key = "sk-..."' > .streamlit/secrets.toml
streamlit run main.py
```

## Configuration
| Variable | Purpose |
|:--|:--|
| `api_key` in `.streamlit/secrets.toml` | OpenAI API key |

## Tech stack
Python, LangChain, OpenAI GPT-4, HuggingFace BGE embeddings, FAISS, Streamlit

## Notes
`projectenv/` is a committed virtual environment and is not needed; create your own as shown above.
