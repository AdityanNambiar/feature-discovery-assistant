import React, { useState, useRef, useEffect } from "react";
import "./App.css";

const App = () => {
  const [messages, setMessages] = useState([]);
  const [userMessage, setUserMessage] = useState("");
  const [isLoading, setIsLoading] = useState(false);
  const bottomRef = useRef(null);

  const sendMessage = async () => {
    if (!userMessage.trim()) return;

    const newMessages = [...messages, { sender: "user", text: userMessage }];
    setMessages(newMessages);
    setUserMessage("");
    setIsLoading(true);

    try {
      const response = await fetch("http://localhost:8000/ask", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ question: userMessage }),
      });

      const data = await response.json();

      if (data.answer) {
        setMessages((prev) => [
          ...prev,
          {
            sender: "bot",
            text: data.answer,
            source: data.source || "Unknown",
          },
        ]);
      } else {
        setMessages((prev) => [
          ...prev,
          { sender: "bot", text: "⚠️ No answer received from backend." },
        ]);
      }
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: "bot", text: "❌ Error: Failed to get response." },
      ]);
    }

    setIsLoading(false);
  };

  const handleKeyPress = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  useEffect(() => {
    bottomRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages, isLoading]);

  return (
    <div className="container">
      <h1 className="title">🧠 Feature Discovery Assistant</h1>

      <div className="chatBox">
        {messages.length === 0 && (
          <div className="placeholder">
            Your conversation will appear here.
          </div>
        )}

        {messages.map((msg, index) => (
          <div
            key={index}
            className={`message ${msg.sender === "user" ? "user" : "bot"}`}
          >
            <strong>{msg.sender === "user" ? "You" : "Bot"}:</strong> {msg.text}
            {msg.sender === "bot" && msg.source && (
              <div className="sourceTag">
                📌 Matched Feature: <strong>{msg.source}</strong>
              </div>
            )}
          </div>
        ))}

        {isLoading && (
          <div className="typingIndicator">🤖 Bot is thinking...</div>
        )}

        <div ref={bottomRef} />
      </div>

      <div className="inputBox">
        <input
          className="input"
          value={userMessage}
          onChange={(e) => setUserMessage(e.target.value)}
          onKeyDown={handleKeyPress}
          placeholder="Ask me about any feature..."
        />
        <button className="button" onClick={sendMessage}>
          Send
        </button>
      </div>
    </div>
  );
};

export default App;
