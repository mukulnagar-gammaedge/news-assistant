'''from dotenv import load_dotenv
import os
from graph import build_graph

load_dotenv() 

def run():
    graph = build_graph()

    # News example
    result1 = graph.invoke({"question": "Give me latest news headlines"})
    print("News Result:", result1)

    # PDF example
    #result2 = graph.invoke({"question": "Summarize the PDF about AI."})
    #print("PDF Result:", result2)

if __name__ == "__main__":
    run()
'''


from dotenv import load_dotenv
import os
from graph import build_graph

load_dotenv() 

# --- Input Guardrails ---
def input_guardrails(user_input: str, allowed_tasks: list):
    suspicious_patterns = ["ignore instructions", "system prompt", "disable safety"]
    if any(p in user_input.lower() for p in suspicious_patterns):
        return "Rejected: Prompt injection attempt"

    if not any(task in user_input.lower() for task in allowed_tasks):
        return "Rejected: Out of scope"

    return "Accepted"

def run():
    graph = build_graph()

    # News example
    user_question = "give me latest news"
    guardrail_result = input_guardrails(user_question, allowed_tasks=["news", "summarize", "analyze"])

    if guardrail_result != "Accepted":
        print("Input blocked:", guardrail_result)
        return

    result1 = graph.invoke({"question": user_question})
    print("News Result:", result1)

    # PDF example
    # user_question = "Summarize the PDF about AI."
    # guardrail_result = input_guardrails(user_question, allowed_tasks=["summarize"])
    # if guardrail_result != "Accepted":
    #     print("Input blocked:", guardrail_result)
    #     return
    # result2 = graph.invoke({"question": user_question})
    # print("PDF Result:", result2)

if __name__ == "__main__":
    run()
