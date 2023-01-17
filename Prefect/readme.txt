prefect deployment build ./flows.py:my_flow -n git-flow -sb github-repository/dbt-bq-repo -q test -o dbt-bq-repo-git-deployment.yaml
prefect deployment apply dbt-bq-repo-git-deployment.yaml