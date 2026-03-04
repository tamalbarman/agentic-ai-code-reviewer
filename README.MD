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

## 🧠 System Architecture

The AI Code Review Agent integrates with GitHub Pull Requests and automatically reviews code changes using a local LLM.

```mermaid
flowchart TD
A[Developer Opens Pull Request] --> B[GitHub Repository]
B --> C[GitHub API]
C --> D[Code Review Agent]
D --> E[Extract PR Code Diff]
E --> F[Prompt Builder]
F --> G[Local LLM via Ollama]
G --> H[AI Code Analysis]
H --> I[Generate Review Feedback]
I --> J[GitHub Comment Bot]
J --> K[Post Comment on Pull Request]
K --> L[Developer Receives AI Code Review]
```mermaid
