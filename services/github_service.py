import os
from github import Github


class GitHubService:

    def __init__(self):
        token = os.getenv("GITHUB_TOKEN")

        if not token:
            raise Exception("GITHUB_TOKEN not set")

        self.github = Github(token)

    def get_pull_request_diff(self, repo_name, pr_number):

        repo = self.github.get_repo(repo_name)

        pr = repo.get_pull(pr_number)

        diff = ""

        files = pr.get_files()

        for file in files:
            diff += f"\nFile: {file.filename}\n"
            diff += file.patch + "\n"

        return diff

    def comment_on_pr(self, repo_name, pr_number, comment):

        repo = self.github.get_repo(repo_name)

        pr = repo.get_pull(pr_number)

        pr.create_issue_comment(comment)