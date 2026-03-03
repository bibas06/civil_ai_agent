async def intent_agent(state):
    q = state["query"].lower()
    has_numbers = any(char.isdigit() for char in q)

    if "bbs" in q and not has_numbers:
        state["intent"] = "BBS_CONCEPT"
    elif "bbs" in q and has_numbers:
        state["intent"] = "BBS_CALC"
    elif "is" in q or "code" in q:
        state["intent"] = "CODE"
    else:
        state["intent"] = "SITE"

    return state
