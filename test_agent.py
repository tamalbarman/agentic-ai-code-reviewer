import asyncio
from agents.review_agent import CodeReviewAgent


async def run():

    agent = CodeReviewAgent()

    diff = """
- def calculate(x,y):
-  return x+y
+ def add_numbers(x: int, y: int) -> int:
+     return x + y
"""

    review = await agent.review_diff(diff)

    print("\nAI PR Review\n")
    print(review)


asyncio.run(run())