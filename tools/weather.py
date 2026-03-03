import httpx
from app.config import WEATHER_API_KEY

async def get_weather(city):
    async with httpx.AsyncClient() as client:
        r = await client.get(
            "http://api.weatherapi.com/v1/current.json",
            params={"key": WEATHER_API_KEY, "q": city}
        )
        return r.json()
