def slab_bbs(length, width, spacing, dia, cover=0.025):
    clear_length = length - 2 * cover
    clear_width = width - 2 * cover

    bars_x = int(clear_width / spacing) + 1
    bars_y = int(clear_length / spacing) + 1

    total_length = (
        bars_x * clear_length +
        bars_y * clear_width
    )

    steel_weight = total_length * (dia ** 2 / 162)

    return {
        "bars_x_direction": bars_x,
        "bars_y_direction": bars_y,
        "total_steel_length_m": round(total_length, 2),
        "steel_weight_kg": round(steel_weight, 2),
        "assumptions": {
            "clear_cover_m": cover,
            "unit_weight_formula": "d² / 162"
        }
    }

async def bbs_agent(state):
    if not state["bbs_input"]:
        state["bbs_data"] = {
            "error": "Missing slab dimensions, bar dia or spacing."
        }
        return state

    p = state["bbs_input"]
    state["bbs_data"] = slab_bbs(
        length=p["length"],
        width=p["width"],
        spacing=p["spacing"],
        dia=p["dia"]
    )
    return state
