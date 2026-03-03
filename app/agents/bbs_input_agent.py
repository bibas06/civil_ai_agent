import re

async def bbs_input_agent(state):
    query = state["query"].lower()
    nums = re.findall(r"\d+\.?\d*", query)

    if len(nums) < 4:
        state["bbs_input"] = None
        return state

    state["bbs_input"] = {
        "length": float(nums[0]),
        "width": float(nums[1]),
        "dia": float(nums[2]),
        "spacing": float(nums[3]) / 1000
    }
    return state
