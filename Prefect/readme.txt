prefect deployment build ./flows.py:my_flow -n git-flow -sb github/dbt-bq-repo-2 -q test -o dbt-bq-repo-git-deployment.yaml
prefect deployment apply dbt-bq-repo-git-deployment.yaml