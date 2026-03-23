# 📰 News Assistant with LangGraph & Groq

A modular AI assistant built with **LangGraph**, integrating **live news headlines** via NewsAPI and **document Q&A** via RAG over PDFs. The assistant intelligently routes queries to the right branch and generates concise answers using **Groq LLM**.

---

## 🚀 Features
- **Decision Node**: Classifies queries into *news* or *document*.
- **News Node**: Fetches top headlines from [NewsAPI](https://newsapi.org).
- **RAG Node**: Loads a PDF, splits into chunks, embeds with HuggingFace, and retrieves relevant context.
- **Answer Node**: Uses Groq LLM (`llama3-8b-8192`) to generate concise, human‑like answers.
- **Graph Wiring**: Conditional edges ensure only one branch runs per query.

---

news-assistant/
│── main.py
│── graph.py
│── nodes/
│   ├── decision_node.py
│   ├── news_node.py
│   ├── rag_node.py
│   ├── answer_node.py
│── sample.pdf
│── requirements.txt
│── .env




---

## 🔑 Environment Variables
Create a `.env` file in the project root:

```env
NEWS_API_KEY=your_newsapi_key_here
GROQ_API_KEY=your_groq_api_key_here
📦 Installation
bash
git clone https://github.com/yourusername/news-assistant.git
cd news-assistant
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
pip install -r requirements.txt
▶️ Usage
Run the assistant:

bash
python main.py
Example outputs:

News Query:

Code
News Result: {'final_answer': 'Latest headlines: ...'}
PDF Query:

Code
PDF Result: {'final_answer': 'Summary: ...'}
📚 Requirements
txt
langgraph>=0.0.45
langchain>=0.3.0
langchain-community>=0.0.30
langchain-text-splitters>=0.0.1
langchain-huggingface>=0.0.3
sentence-transformers>=2.2.2
chromadb>=0.5.0
pypdf>=3.17.0
requests>=2.31.0
langchain-groq>=0.1.0
python-dotenv>=1.0.0
🛠 How It Works
Decision Node → routes query to news or rag.

News Node → fetches headlines from NewsAPI.

RAG Node → retrieves context from PDF via embeddings.

Answer Node → Groq LLM generates the final answer.
