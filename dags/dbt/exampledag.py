from cosmos import DbtDag, ProjectConfig, ProfileConfig, ExecutionConfig
from datetime import datetime
import os
from pathlib import Path

# Dentro do contêiner do Astro CLI, as DAGs ficam mapeadas em /usr/local/airflow/dags
DBT_PROJECT_PATH = Path("/usr/local/airflow/dags/dbt/projeto_prod")

# No Linux do contêiner, os binários ficam na pasta 'bin' (e não 'Scripts')
DBT_EXECUTABLE = Path(os.environ.get("AIRFLOW_HOME", "/usr/local/airflow")) / "dbt_venv" / "bin" / "dbt"

my_dbt_dag = DbtDag(
    project_config=ProjectConfig(
        dbt_project_path=str(DBT_PROJECT_PATH),
    ),
    profile_config=ProfileConfig(
        profile_name="projeto_prod",
        target_name="dev",
        profiles_yml_filepath=str(DBT_PROJECT_PATH / "profiles.yml")
    ),
    execution_config=ExecutionConfig(
        dbt_executable_path=str(DBT_EXECUTABLE)
    ),
    schedule="@daily",
    start_date=datetime(2024, 1, 1),
    catchup=False,
    dag_id="projeto_prod"
)