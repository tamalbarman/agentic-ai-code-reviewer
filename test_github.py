from github import Github
from dotenv import load_dotenv
import os

load_dotenv()

token = os.getenv("GITHUB_TOKEN")

g = Github(token)

user = g.get_user()

print(user.login)