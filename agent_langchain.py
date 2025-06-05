#!/usr/bin/env python3
# agent_langchain.py
from typing import Dict, Any
import os
import uuid
from dotenv import load_dotenv
from langchain.agents import initialize_agent, Tool
from langchain_community.llms import OpenAI
import requests
from requests.exceptions import RequestException

def call_agent2(message: str) -> str:
    """
    Send a message to the LlamaIndex agent and get its response.
    
    Args:
        message (str): The message to send to the agent
        
    Returns:
        str: The response from the agent
        
    Raises:
        RequestException: If there's an error communicating with the agent
    """
    try:
        a2a_payload = {
            "id": str(uuid.uuid4()),
            "sender": "langchain_agent",
            "receiver": "llamaindex_agent",
            "message": {
                "type": "text",
                "content": message
            }
        }
        res = requests.post("http://localhost:8002/receive", json={"message": message}, timeout=10)
        res.raise_for_status()
        return res.json()["reply"]
    except RequestException as e:
        raise RequestException(f"Error communicating with LlamaIndex agent: {str(e)}")

def setup_agent():
    """
    Initialize and return the LangChain agent with necessary tools.
    
    Returns:
        Any: Initialized LangChain agent
    """
    # Load environment variables
    load_dotenv()
    
    # Ensure OpenAI API key is set
    if not os.getenv("OPENAI_API_KEY"):
        raise ValueError("OPENAI_API_KEY environment variable is not set")
    
    llm = OpenAI(temperature=0.5)
    tools = [Tool(
        name="TalkToLlamaAgent",
        func=call_agent2,
        description="Talk to the second agent"
    )]
    
    return initialize_agent(tools, llm, agent="zero-shot-react-description", verbose=True)

if __name__ == "__main__":
    try:
        agent = setup_agent()
        query = "Ask the other agent: What is your knowledge domain?"
        response = agent.run(query)
        print("LangChain Agent Response:", response)
    except Exception as e:
        print(f"Error: {str(e)}")
