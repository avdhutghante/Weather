import React, { useState } from 'react';
import axios from 'axios';
import './App.css';

function App() {
  const [message, setMessage] = useState('');
  const [response, setResponse] = useState('');
  const [loading, setLoading] = useState(false);

  const handleSend = async () => {
    if (!message.trim()) return;

    setLoading(true);
    setResponse('');

    try {
      const result = await axios.post('http://localhost:8000/ask', {
        message: message
      });
      setResponse(result.data.response);
    } catch (error) {
      setResponse('Error: Unable to connect to the server. Make sure the backend is running.');
    } finally {
      setLoading(false);
    }
  };

  const handleKeyPress = (e) => {
    if (e.key === 'Enter') {
      handleSend();
    }
  };

  return (
    <div className="App">
      <h1>🌤️ Weather Assistant</h1>
      
      <div className="input-container">
        <input
          type="text"
          placeholder="Ask about weather (e.g., 'What's the weather in Pune?')"
          value={message}
          onChange={(e) => setMessage(e.target.value)}
          onKeyPress={handleKeyPress}
          disabled={loading}
        />
        <button onClick={handleSend} disabled={loading}>
          Send
        </button>
      </div>

      {loading && <div className="loading">Getting weather information...</div>}
      
      {response && (
        <div className="response">
          <strong>Response:</strong>
          <p>{response}</p>
        </div>
      )}
    </div>
  );
}

export default App;
