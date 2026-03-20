def decision_node(state):
    question = state.get("question", "").lower()
    if "news" in question or "headline" in question:
        route = "news"
    else:
        route = "pdf"
    print("This is decision node")
    print(f"[Decision] Routing to: {route}")
    return {**state, "route": route}
