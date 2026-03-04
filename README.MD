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


This will render directly on GitHub.

---

# 2. Project Architecture Overview (Add to README)

Also add this:

```markdown
## ⚙️ Architecture Overview

The system works as follows:

1. A developer creates or updates a **GitHub Pull Request**
2. The agent fetches **PR code changes using GitHub API**
3. Code diffs are extracted and formatted
4. The diff is sent to a **Local LLM (Ollama)**
5. The LLM analyzes the code for:
   - Bugs
   - Code quality issues
   - Performance problems
   - Security risks
6. The AI generates structured review feedback
7. The system posts the review comment directly to the PR
