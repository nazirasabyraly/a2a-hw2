# 🤖 LangChain ↔ LlamaIndex A2A Agent Demo

This project demonstrates an agent-to-agent (A2A) communication pattern using LangChain and LlamaIndex.

## 📁 Structure

- `agent_langchain.py`: LangChain agent that sends a message to the LlamaIndex agent over HTTP.
- `agent_llamaindex.py`: FastAPI app that hosts a LlamaIndex agent.
- `.env.example`: Template for OpenAI key and port config.
- `requirements.txt`: List of required dependencies.

## 🚀 Getting Started

1. Clone the repo:

```bash
git clone https://github.com/yourusername/a2a-hw2.git
cd a2a-hw2
```
2. Setup Environment

```bash
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
Add your OPENAI_API_KEY to the .env file.
```
3. 🧠 Running the Agents

```bash
Terminal 1: LlamaIndex Agent Server
python agent_llamaindex.py
Terminal 2: LangChain Agent Client
bash
Копировать
Редактировать
python agent_langchain.py
```
4. ✅  Example Output

```bash
> Entering new AgentExecutor chain...
 I should ask the other agent about their knowledge domain to learn more.
Action: TalkToLlamaAgent
Action Input: "What is your knowledge domain?"
Observation: I am an AI digital assistant and my knowledge domain includes a wide range of topics such as general knowledge, technology, science, history, entertainment, and more. I am constantly learning and updating my knowledge base to provide accurate and helpful information to users.
Thought: This information will help me understand the capabilities and limitations of the other agent.
Action: TalkToLlamaAgent
Action Input: "Can you provide some examples of topics within your knowledge domain?"
Observation: Sure! Here are some examples of topics within the field of artificial intelligence:

1. Machine learning algorithms  
2. Natural language processing  
3. Deep learning architectures  
4. Computer vision techniques  
5. Reinforcement learning  
6. Robotics and autonomous systems  
7. Ethical considerations in AI development  
8. AI applications in healthcare, finance, and other industries  
9. AI bias and fairness  
10. Quantum computing and AI.

Final Answer: The other agent's knowledge domain includes a wide range of topics within the field of artificial intelligence, such as machine learni
```
https://drive.google.com/file/d/1SQvpvf3WXa3SYv7v6Am9XRnSy2hszIfj/view?usp=sharing
