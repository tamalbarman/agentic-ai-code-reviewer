AI Code Review Agent

An Agentic AI system that automatically reviews GitHub Pull Requests using LLMs.

This project builds an AI agent that reads code changes from GitHub PRs, analyzes them using a local Large Language Model (Ollama), and generates automated code review feedback.

The system simulates how a senior engineer reviews pull requests by detecting bugs, code quality issues, performance risks, and improvement suggestions.

Demo

Example workflow:

Developer opens Pull Request
↓
AI Agent reads PR code diff
↓
LLM analyzes code changes
↓
AI generates review feedback
↓
Bot posts comment on PR

Example output:

AI Code Review

Bugs:

- Missing input validation

Code Quality:

- Function name could be more descriptive
- Add type hints for better readability

Suggested Improvement:

- Add docstring explaining function purpose
  System Architecture
  flowchart TD

A[Developer Opens Pull Request] --> B[GitHub Repository]

B --> C[GitHub API]

C --> D[AI Code Review Agent]

D --> E[Extract Code Diff]

E --> F[Prompt Builder]

F --> G[Local LLM via Ollama]

G --> H[Code Analysis]

H --> I[Generate Review Feedback]

I --> J[GitHub Comment Bot]

J --> K[Post Review Comment on PR]

Key Features

Automatic GitHub Pull Request analysis

Extracts code diffs from commits

Uses LLMs to perform code review

Detects

Bugs

Code quality issues

Performance concerns

Security risks

Posts AI-generated comments directly to GitHub PR

Fully local LLM support using Ollama

Modular Agent-based architecture

Tech Stack
Component Technology
Backend Python
AI Model Ollama (Mistral / LLaMA)
GitHub Integration PyGithub
Agent System Custom Agent Workflow
Async Processing asyncio + httpx
Version Control Git + GitHub
Project Structure
agentic-ai-code-reviewer
│
├── agents
│ └── review_agent.py
│
├── services
│ └── github_service.py
│
├── llm
│ └── ollama_client.py
│
├── test_pr_reader.py
├── requirements.txt
├── .gitignore
└── README.md
Installation

Clone the repository

git clone https://github.com/yourusername/agentic-ai-code-reviewer.git
cd agentic-ai-code-reviewer

Create virtual environment

python -m venv venv

Activate environment

Windows

venv\Scripts\activate

Install dependencies

pip install -r requirements.txt
Install Ollama

Download Ollama

https://ollama.com

Pull an LLM model

ollama pull mistral

Start Ollama server

ollama serve
Setup GitHub Token

Create a GitHub Personal Access Token.

Scopes required:

repo

Set environment variable.

Windows PowerShell:

$env:GITHUB_TOKEN="your_token_here"
Running the AI Code Reviewer

Run the test script:

python test_pr_reader.py

Example output:

Reading repo: tamal/genai-rag-document-qa
PR number: 1

Pull Request Code Changes:

File: hello.py
+print("hello")

AI Code Review:

- Missing docstring
- Consider adding type hints
- Use logging instead of print in production

The agent will then post the review comment directly to the Pull Request.

Example Use Case

Developer creates PR:

hello.py
print("hello")

AI agent reviews code and comments:

AI Code Review

Code Quality Issues:

- Missing documentation
- No type hints

Suggested Fix:

def main():
print("hello")

if **name** == "**main**":
main()
Future Improvements

GitHub Webhook automation

Multi-agent review system

Security agent

Performance agent

Style agent

FastAPI service for PR triggers

Slack / Discord notifications

CI/CD integration

Learning Outcomes

This project demonstrates:

Building Agentic AI systems

Integrating LLMs with developer workflows

Using GitHub APIs for automation

Creating AI-powered developer tools

Author

Tamal
AI / GenAI Developer

Projects:

RAG Document QA System

AI Code Review Agent

GenAI Real Estate Assistant

License

MIT License

If you like this project

Give it a ⭐ on GitHub!
