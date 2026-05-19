# Beginner AI Agent Tutor Project

This is my first AI agent project built with the OpenAI Agents SDK.

The project allows the user to choose between two different AI tutor agents:

1. Math Tutor
2. History Tutor

After the user chooses an agent, they can ask a question, and the selected agent will answer.

---

## What I Built

In this project, I created a simple command-line AI agent application using Python.

The app includes:

- A Math Tutor agent
- A History Tutor agent
- User input from the terminal
- Agent selection logic
- A custom function tool for math jokes
- Web search tool support for the history agent
- Async execution using `asyncio`
- Environment variable loading with `python-dotenv`

---

## How It Works

The user is first asked to choose an agent:

```text
1: Math tutor
2: History tutor
