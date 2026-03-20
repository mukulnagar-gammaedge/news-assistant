import os, requests

def news_node(state):
    api_key = "7144a176231344aa9ade55b1c9904284"
    url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={api_key}"
    response = requests.get(url).json()

    if response.get("status") != "ok":
        context = "Could not fetch news."
    else:
        articles = response.get("articles", [])[:3]
        headlines = [a["title"] for a in articles]
        context = " | ".join(headlines)

    #print("This is news node")
    #print(headlines)
    #print(articles)

    return {**state, "context": context}


