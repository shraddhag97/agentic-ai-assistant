## Agentic AI Research Assistant

An agentic AI system that performs autonomous web research on any topic and generates a structured report using LLM reasoning and tool usage.

This project demonstrates how modern AI agents search, read, and synthesize information instead of just responding to prompts.

---

## What this project does

User enters a topic like:

* AI in healthcare
* Future of electric vehicles
* Impact of AI on banking

The agent:

1. Searches the web
2. Extracts content from top sources
3. Analyzes information using LLM
4. Generates structured research report

---

## Architecture

User Topic
→ Web Search Tool
→ Content Extraction
→ LLM Analysis
→ Structured Research Report

This demonstrates a true **agentic workflow** using tools + reasoning.

---

## Tech Stack

* Python
* OpenAI / LLM API
* Streamlit
* BeautifulSoup (web scraping)
* Requests
* python-dotenv

---

## Project Structure

agentic-ai-assistant/

* main.py        → Streamlit UI
* agent.py       → agent orchestration logic
* tools.py       → web search + extraction tools
* .env           → API key (not pushed)
* requirements.txt
* README.md

---

## Setup Instructions

### 1. Clone repo

git clone <your_repo_url>
cd agentic-ai-assistant

### 2. Create virtual environment

python3 -m venv agentic_env
source agentic_env/bin/activate

### 3. Install dependencies

pip install -r requirements.txt

### 4. Add OpenAI key

Create `.env` file:

OPENAI_API_KEY=your_key_here

### 5. Run app

streamlit run main.py

---

## Key Features

* Tool-using LLM agent
* Real-time web research
* Multi-step reasoning
* Structured report generation
* Streamlit UI
* Modular agent architecture

---

## Example Use Cases

* Market research
* Tech trend analysis
* Quick topic understanding
* Competitive analysis

---
