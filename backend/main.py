from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from dotenv import load_dotenv
import os
import re
from pathlib import Path
from weather_tool import get_weather

env_path = Path(__file__).parent / ".env"
load_dotenv(dotenv_path=env_path)

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

class QueryRequest(BaseModel):
    message: str

OPENROUTER_API_KEY = "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"

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",
    api_key=OPENROUTER_API_KEY,
    base_url="https://openrouter.ai/api/v1",
    temperature=0.7
)

def extract_city(query: str) -> str:
    """Extract city name from user query using simple text processing."""

    query = query.lower()
    remove_words = ['what', 'whats', "what's", 'is', 'the', 'weather', 'whether', 'of', 'in', 'for', 'today', 'now', 'current', 'tell', 'me', 'about', 'how', 'like', '?', '.', '!']
    
    words = query.split()
    city_words = [w for w in words if w not in remove_words]
    city = ' '.join(city_words).strip()

    return city.title() if city else "Unknown"

@app.get("/")
def read_root():
    return {"message": "Weather API is running"}

@app.post("/ask")
async def ask_weather(query: QueryRequest):
    """
    Endpoint to handle user queries about weather.
    """
    try:

        city = extract_city(query.message)
        
    
        weather_data = get_weather(city)
        
        messages = [
            SystemMessage(content="You are a helpful weather assistant. Given the weather data, provide a friendly response to the user."),
            HumanMessage(content=f"User asked: {query.message}\n\nWeather data: {weather_data}\n\nProvide a friendly response about the weather.")
        ]
        response = llm.invoke(messages)
        
        return {"response": response.content}
    except Exception as e:
        return {"response": f"Sorry, I encountered an error: {str(e)}"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
