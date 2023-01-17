from prefect import task, flow
from prefect.filesystems import GitHub



@flow()
def my_flow():
    github_block = GitHub.load("dbt-bq-repo-2")
    print("What is your favorite number?")
    return 42, github_block

