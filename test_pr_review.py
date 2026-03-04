import asyncio
from agents.review_agent import CodeReviewAgent
from services.github_service import GitHubService


async def run():

    github = GitHubService()

    repo_name = "OWNER/REPO_NAME"

    pr_number = 1

    diff = github.get_pull_request_diff(repo_name, pr_number)

    agent = CodeReviewAgent()

    review = await agent.review_diff(diff)

    print("\nAI Pull Request Review\n")

    print(review)


asyncio.run(run())