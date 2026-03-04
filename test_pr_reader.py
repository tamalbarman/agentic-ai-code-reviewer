import asyncio
from services.github_service import GitHubService
from agents.review_agent import CodeReviewAgent


async def run():

    repo_name = "tamalbarman/genai-rag-document-qa"
    pr_number = 1

    github = GitHubService()

    print("Reading repo:", repo_name)
    print("PR number:", pr_number)

    diff = github.get_pull_request_diff(repo_name, pr_number)

    print("\nPull Request Code Changes:\n")
    print(diff)

    agent = CodeReviewAgent()

    review = await agent.review_diff(diff)

    print("\nAI Code Review:\n")
    print(review)

    # Post comment to GitHub PR
    github.comment_on_pr(repo_name, pr_number, review)

    print("\nAI review posted to GitHub PR!")


asyncio.run(run())