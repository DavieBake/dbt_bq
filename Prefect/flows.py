from prefect import task, flow
from prefect_github.repository import GitHubRepository



@flow()
def my_flow():
    github_repository_block = GitHubRepository.load("dbt-bq-repo2")
    print("What is your favorite number?")
    return 42, github_repository_block

