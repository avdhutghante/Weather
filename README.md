# Weather App

A simple weather application with React frontend and FastAPI backend using Langchain + OpenRouter.

## Features
- Ask about weather for any city
- AI-powered agent using Langchain
- Clean and simple UI
- Real-time weather data

## Project Structure
```
project weather/
├── backend/
│   ├── main.py              # FastAPI application
│   ├── weather_tool.py      # Weather fetching tool
│   ├── requirements.txt     # Python dependencies
│   └── .env                 # Environment variables (create this)
├── frontend/
│   ├── src/
│   │   ├── App.js          # Main React component
│   │   ├── App.css         # Styling
│   │   └── index.js        # Entry point
│   ├── public/
│   │   └── index.html      # HTML template
│   └── package.json        # Node dependencies
└── README.md
```

## Setup Instructions

### 1. Get API Keys

**OpenRouter API Key:**
1. Go to https://openrouter.ai/
2. Sign up and get your API key
3. This is free for the model we're using (llama-3.1-8b-instruct)

**OpenWeatherMap API Key:**
1. Go to https://openweathermap.org/api
2. Sign up for a free account
3. Get your API key (free tier allows 1000 calls/day)

### 2. Backend Setup

```bash
# Navigate to backend folder
cd backend

# Create virtual environment
python -m venv venv

# Activate virtual environment
# On Windows:
venv\Scripts\activate
# On Mac/Linux:
# source venv/bin/activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
copy .env.example .env

# Edit .env file and add your API keys:
# OPENROUTER_API_KEY=your_actual_openrouter_key
# WEATHER_API_KEY=your_actual_weather_key
```

### 3. Frontend Setup

```bash
# Open a new terminal
# Navigate to frontend folder
cd frontend

# Install dependencies
npm install

# If you get errors, try:
# npm install --legacy-peer-deps
```

### 4. Running the Application

**Terminal 1 - Backend:**
```bash
cd backend
venv\Scripts\activate
python main.py
```
Backend will run on http://localhost:8000

**Terminal 2 - Frontend:**
```bash
cd frontend
npm start
```
Frontend will run on http://localhost:3000

### 5. Using the App

1. Open http://localhost:3000 in your browser
2. Type a question like:
   - "What's the weather in Pune?"
   - "Weather of Mumbai today?"
   - "How's the weather in New York?"
3. Click "Send" or press Enter
4. The AI agent will fetch and display the weather

## How It Works

1. **User Input**: User types a weather question in the React frontend
2. **API Call**: Frontend sends the question to FastAPI backend
3. **Langchain Agent**: Backend uses Langchain agent with OpenRouter LLM
4. **Tool Selection**: Agent decides if it needs to use the weather tool
5. **Weather Fetch**: Tool calls OpenWeatherMap API for real weather data
6. **Response**: Agent formulates a natural response and sends back to frontend
7. **Display**: Frontend shows the weather information

## Technologies Used

- **Frontend**: React, Axios
- **Backend**: FastAPI, Python
- **AI**: Langchain, OpenRouter (Meta Llama 3.1)
- **Weather Data**: OpenWeatherMap API

## Troubleshooting

**Backend won't start:**
- Make sure virtual environment is activated
- Check if all dependencies are installed
- Verify .env file has correct API keys

**Frontend won't start:**
- Try `npm install --legacy-peer-deps`
- Clear npm cache: `npm cache clean --force`

**Can't connect to backend:**
- Make sure backend is running on port 8000
- Check CORS settings in main.py

**Weather not working:**
- Verify WEATHER_API_KEY in .env
- Check if city name is spelled correctly
- Free tier has 1000 calls/day limit

## Example Queries

- "What's the weather in Pune?"
- "How's the weather in London today?"
- "Tell me the temperature in Tokyo"
- "Is it raining in Mumbai?"
- "Weather of Paris"

---

Built with ❤️ using React, FastAPI, and Langchain
