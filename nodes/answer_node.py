'''import os
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
'''

import os
from langchain_groq import ChatGroq
import re

llm = ChatGroq(
    model="llama-3.1-8b-instant",
    api_key="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"
)

def output_guardrails(response: str, context: str = ""):
    issues = []

    unsafe_keywords = ["suicide", "bomb", "hack password"]
    if any(k in response.lower() for k in unsafe_keywords):
        issues.append("Unsafe content detected")

    if re.search(r"[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}", response):
        issues.append("Contains possible email address (PII)")
    if re.search(r"\b\d{10}\b", response):
        issues.append("Contains possible phone number (PII)")

    if context and not any(word in response.lower() for word in context.lower().split()):
        issues.append("Unsupported claim or irrelevant response")

    return issues

def answer_node(state):
    question = state.get("question", "")
    context = state.get("context", "")
    response = llm.invoke(f"Question: {question}\nContext: {context}\nAnswer in one line:")

    issues = output_guardrails(response.content, context)
    if issues:
        return {"status": "blocked", "issues": issues}
    return {"status": "ok", "final_answer": response.content}
