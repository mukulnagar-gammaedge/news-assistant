import os
from langchain_groq import ChatGroq

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="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"
)

def answer_node(state):
    question = state.get("question", "")
    context = state.get("context", "")
    response = llm.invoke(f"Question: {question}\nContext: {context}\nAnswer in one line:")
    return {"final_answer": response.content}
