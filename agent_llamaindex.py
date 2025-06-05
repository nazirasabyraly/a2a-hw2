#!/usr/bin/env python3
# agent_llamaindex.py
import os
from typing import Dict, Any

from dotenv import load_dotenv
from fastapi import FastAPI, Request, HTTPException
from llama_index.llms.openai import OpenAI
from llama_index.agent.openai import OpenAIAgent
import uvicorn

import uvicorn

# Load environment variables
load_dotenv()

# Check for OpenAI API key
if not os.getenv("OPENAI_API_KEY"):
    raise ValueError("OPENAI_API_KEY environment variable is not set")

app = FastAPI(title="LlamaIndex Agent API")

def setup_agent() -> OpenAIAgent:
    llm = OpenAI(temperature=0.7)
    agent = OpenAIAgent.from_tools([], llm=llm, verbose=True)
    print("🧪 Проверка агента:", agent)
    return agent

    

@app.post("/receive")
async def receive_message(request: Request) -> Dict[str, str]:
    try:
        print("🔹 Получен запрос")
        data = await request.json()
        print("🔹 JSON данных:", data)

        message = data.get("message", {})
        content = message if isinstance(message, str) else message.get("content", "")
        print("🔹 Извлечён контент:", content)

        if not content:
            raise HTTPException(status_code=400, detail="No message content provided")

        agent = setup_agent()
        print("🔹 Агент инициализирован")

        reply = agent.chat(content)
        print("🔹 Ответ от агента:", reply)

        return {"reply": str(reply)}

    except Exception as e:
        print("❌ Ошибка:", str(e))  # Важная строка!
        raise HTTPException(status_code=500, detail=f"Error processing request: {str(e)}")


@app.get("/health")
async def health_check() -> Dict[str, str]:
    """
    Health check endpoint to verify the service is running.
    
    Returns:
        Dict[str, str]: Status message
    """
    return {"status": "healthy"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8002)
