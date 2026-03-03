from app.tools.weather import get_weather
from app.tools.materials import get_material_prices

async def site_agent(state):
    state["weather_data"] = await get_weather("Durgapur")
    state["material_data"] = await get_material_prices()
    return state
