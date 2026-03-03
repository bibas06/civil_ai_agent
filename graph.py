from langgraph.graph import StateGraph
from state import CivilState
from agents.intent_agent import intent_agent
from agents.bbs_input_agent import bbs_input_agent
from agents.bbs_agent import bbs_agent
from agents.bbs_concept_agent import bbs_concept_agent
from agents.site_agent import site_agent
from agents.code_agent import code_agent

def build_graph():
    g = StateGraph(CivilState)

    g.add_node("intent", intent_agent)
    g.add_node("bbs_input", bbs_input_agent)
    g.add_node("bbs_calc", bbs_agent)
    g.add_node("bbs_concept", bbs_concept_agent)
    g.add_node("site", site_agent)
    g.add_node("code", code_agent)

    g.set_entry_point("intent")

    g.add_conditional_edges(
        "intent",
        lambda s:
            "bbs_concept" if s["intent"] == "BBS_CONCEPT"
            else "bbs_input" if s["intent"] == "BBS_CALC"
            else "code" if s["intent"] == "CODE"
            else "site"
    )

    g.add_edge("bbs_input", "bbs_calc")
    g.add_edge("bbs_calc", "__end__")
    g.add_edge("bbs_concept", "__end__")
    g.add_edge("site", "__end__")
    g.add_edge("code", "__end__")

    return g.compile()
