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
