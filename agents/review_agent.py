import asyncio
from services.llm_service import LocalLLM


class CodeReviewAgent:

    def __init__(self):
        self.llm = LocalLLM()

    async def review_diff(self, diff: str):

        prompt = f"""
You are a senior developer reviewing a GitHub pull request.

Analyze the following code diff and provide a review.

Focus on:
- Bugs
- Code quality
- Performance
- Security

GitHub Diff:
{diff}

Return feedback in bullet points.
"""

        review = await self.llm.generate(prompt)

        return review