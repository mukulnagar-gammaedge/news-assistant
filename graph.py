from langgraph.graph import StateGraph
from nodes.decision_node import decision_node
from nodes.news_node import news_node
from nodes.rag_node import rag_node
from nodes.answer_node import answer_node

def build_graph():
    graph = StateGraph(dict)

    graph.add_node("decision", decision_node)
    graph.add_node("news", news_node)
    graph.add_node("rag", rag_node)
    graph.add_node("answer", answer_node)

    graph.add_conditional_edges(
        "decision",
        lambda state: state["route"],
        {
            "news": "news",
            "pdf": "rag"
        }
    )

    graph.add_edge("news", "answer")
    graph.add_edge("rag", "answer")

    graph.set_entry_point("decision")
    graph.set_finish_point("answer")

    return graph.compile()
