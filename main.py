import os
import httpx
from datetime import datetime
from dotenv import load_dotenv
from fastapi import FastAPI
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
load_dotenv()
app = FastAPI()

# Константы
NEWS_API_KEY = os.getenv("NEWS_API_KEY")

# РАЗРЕШАЕМ ЗАПРОСЫ (CORS)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


# 1. Погода
@app.get("/weather")
async def get_weather():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://wttr.in/Astana?format=j1", timeout=5.0)
            data = response.json()
            current = data['current_condition'][0]
            return {
                "city": "Astana",
                "temp": f"{current['temp_C']}°",
                "condition": current['weatherDesc'][0]['value']
            }
    except Exception as e:
        return {"city": "Ошибка", "temp": "??", "condition": str(e)}


# 2. Валюта
@app.get("/currency")
async def get_currency():
    try:
        async with httpx.AsyncClient() as client:
            response = await client.get("https://api.exchangerate-api.com/v4/latest/USD", timeout=5.0)
            data = response.json()
            rates = data.get('rates', {})
            kzt = rates.get('KZT', 0)

            return [
                {"code": "USD", "name": "Доллар США", "rate": f"{kzt:.2f} ₸", "symbol": "$"},
                {"code": "EUR", "name": "Евро", "rate": f"{(kzt / rates.get('EUR', 1)):.2f} ₸", "symbol": "€"},
                {"code": "RUB", "name": "Рубль", "rate": f"{(kzt / rates.get('RUB', 1)):.2f} ₸", "symbol": "₽"}
            ]
    except Exception as e:
        print(f"Currency error: {e}")
        return []  # Возвращаем пустой список, чтобы JS не упал


# 3. Новости
@app.get("/news")
async def get_news():
    url = f"https://newsapi.org/v2/top-headlines?category=technology&language=en&apiKey={NEWS_API_KEY}"
    async with httpx.AsyncClient() as client:
        try:
            response = await client.get(url, timeout=5.0)
            data = response.json()
            articles = data.get("articles", [])
            formatted_news = []

            for i, art in enumerate(articles[:6]):
                raw_date = art.get("publishedAt", "")
                time_str = "Recent"
                if raw_date:
                    try:
                        # Упрощенный парсинг даты для разных форматов
                        dt_part = raw_date.split('T')[1][:5]
                        time_str = dt_part
                    except:
                        time_str = "Now"

                formatted_news.append({
                    "id": i,
                    "title": art.get("title"),
                    "source": art.get("source", {}).get("name"),
                    "time": time_str,
                    "tag": "Tech",
                    "url": art.get("url")
                })
            return formatted_news
        except Exception as e:
            print(f"News error: {e}")
            return [{"id": 0, "title": "API Error", "source": "System", "time": "now", "tag": "Error", "url": "#"}]


# 4. Статика и Главная (ВСЕГДА В КОНЦЕ)
if not os.path.exists("static"):
    os.makedirs("static")

app.mount("/static", StaticFiles(directory="static"), name="static")


@app.get("/")
async def read_index():
    return FileResponse('static/index.html')