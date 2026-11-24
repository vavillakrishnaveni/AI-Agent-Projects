# AI Research Assistant – Agent 01

An AI-powered research assistant built using Python and Google's Gemini API. This project accepts a research topic from the user and generates a structured research report using Large Language Models (LLMs).

## Project Overview

The AI Research Assistant is the first project in my AI Agent Projects collection.

It uses an LLM with predefined system instructions to understand research topics and generate organized, informative reports.

## Features

- Accepts research topics through user input.
- Uses Google's Gemini API for AI-powered text generation.
- Generates structured research reports.
- Includes explanations, applications, benefits, and challenges.
- Provides a meaningful conclusion.
- Uses environment variables to protect API credentials.

## Tech Stack

- **Programming Language:** Python
- **LLM:** Google Gemini
- **SDK:** Google GenAI
- **Environment Management:** Python dotenv
- **Development Environment:** VS Code

## Project Structure

```text
AI-Agent-Projects/
│
├── main.py
├── requirements.txt
├── .env.example
├── .gitignore
└── README.md
```

## Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/vavillakrishnaveni/AI-Agent-Projects.git
```

### 2. Navigate to the project directory

```bash
cd AI-Agent-Projects
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Configure the API key

Create a `.env` file in the project directory.

Add your Gemini API key:

```env
GEMINI_API_KEY=your_actual_api_key
```

Get an API key from [Google AI Studio](https://aistudio.google.com/).

**Security:** Never upload your actual `.env` file or expose your API key publicly.

### 5. Run the application

```bash
python main.py
```

Enter a research topic when prompted.

## Example Input

```text
applications of artificial intelligence
```

The agent is designed to generate a structured research report covering the topic, its applications, benefits, challenges, and conclusion.

## Current Limitations

- Requires an active internet connection.
- Depends on the availability and usage limits of the Gemini API.
- Generated research content should be independently verified.
- Does not currently perform autonomous web research or retrieve verified academic citations.

## Future Enhancements

- Add web search capabilities for real-time research.
- Introduce memory to retain research context.
- Add multiple specialized AI agents.
- Implement agent-to-agent communication.
- Build a multi-agent research workflow using LangGraph.
- Develop a web interface using FastAPI.

## Learning Objectives

Through this project, I am exploring:

- LLM integration with Python.
- Prompt engineering and system instructions.
- API integration and environment variable management.
- Fundamentals of AI agent development.

## Author

**Krishnaveni Vavilla**

B.Tech – Computer Science and Engineering (AI & ML)

[GitHub](https://github.com/vavillakrishnaveni)

---

*This project is part of my hands-on journey into AI Agents and Multi-Agent Systems.*
