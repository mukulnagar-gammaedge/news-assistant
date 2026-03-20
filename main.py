from dotenv import load_dotenv
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
