FROM astrocrpublic.azurecr.io/runtime:3.3-2

# Cria o virtualenv e instala o dbt com o adapter do BigQuery
RUN python -m venv /usr/local/airflow/dbt_venv && \
    /usr/local/airflow/dbt_venv/bin/pip install --no-cache-dir dbt-bigquery astronomer-cosmos