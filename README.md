# dbt_projeto_prod

Este repositório contém o projeto **dbt (Data Build Tool)** de produção para transformação e modelagem de dados no Data Warehouse. Ele serve como a camada de engenharia e análise de dados (Analytics Engineering), estruturando dados brutos em tabelas prontas para análise e BI. O projeto é orquestrado e gerenciado localmente ou em produção utilizando o **Apache Airflow via Astronomer (Astro CLI)**.

---

## 🚀 Estrutura do Projeto

A estrutura padrão deste projeto dbt e as configurações do Astro seguimentam-se da seguinte forma:

*   **`models/`**: Contém as consultas SQL de transformação de dados divididas em camadas (`staging/`, `marts/`).
*   **`macros/`**: Funções SQL reutilizáveis.
*   **`seeds/`**: Arquivos CSV estáticos carregados diretamente no banco de dados.
*   **`tests/`**: Testes de qualidade de dados (ex: asserções de unicidade e não-nulidade).
*   **`dags/`**: Pasta gerenciada pelo Astro que contém os arquivos Python definindo as DAGs (fluxos) do Airflow que orquestram a execução do dbt.
*   **`Dockerfile`**: Arquivo de customização do Astronomer para herdar a imagem do Astro Runtime e instalar pacotes necessários.
*   **`packages.txt`**: Lista de pacotes a nível de sistema operacional (SO) exigidos no container.
*   **`requirements.txt`**: Dependências Python do Airflow (como `astronomer-cosmos` ou `dbt-core`).

---

## 🛠️ Pré-requisitos & Instalação

### 1. Clonar o Repositório
```bash
git clone -b develop https://github.com/suicangi/dbt_projeto_prod.git
cd dbt_projeto_prod
```

### 2. Instalar o Astro CLI
Certifique-se de possuir o Docker instalado e rodando na sua máquina. Instale o Astro CLI:
*   **macOS (Homebrew):** `brew install astronomer/tap/astro`
*   **Windows/Linux:** Siga as instruções oficiais na documentação do Astronomer.

---

## 🌌 Configuração e Execução com Astro (Airflow)

O ambiente do Airflow roda encapsulado em containers gerenciados pelo Astro CLI.

### 1. Iniciar o Ambiente Local do Astro
Para buildar a imagem localmente e iniciar os serviços do Airflow (Webserver, Scheduler, Triggerer e Postgres):
```bash
astro dev start
```
Após a inicialização bem-sucedida, acesse a UI do Airflow pelo navegador em: `http://localhost:8080` (usuário e senha padrão: `admin` / `admin`).

### 2. Comandos Úteis do Astro CLI
*   **Parar o ambiente local:**
    ```bash
    astro dev stop
    ```
*   **Reiniciar o ambiente (aplicar alterações estruturais como no Dockerfile/requirements):**
    ```bash
    astro dev restart
    ```
*   **Verificar os logs dos containers:**
    ```bash
    astro dev logs
    ```
*   **Acessar o terminal interativo de um container (ex: scheduler):**
    ```bash
    astro dev bash --scheduler
    ```

### 3. Conexões e Variáveis no Airflow
Para que as DAGs consigam executar o dbt corretamente dentro do container, configure as credenciais de conexão do banco de dados (equivalentes ao seu `profiles.yml`) diretamente na interface Web do Airflow em **Admin -> Connections**, ou mapeie-as utilizando variáveis de ambiente no arquivo `.env` do projeto.

---

## 🏃 Execução Manual do dbt (Desenvolvimento Local)

Caso prefira validar e testar os modelos dbt isoladamente fora do Airflow:

### 1. Configurar o Ambiente Virtual Python
```bash
python -m venv venv
source venv/bin/activate  # No Windows: venv\Scripts\activate
pip install dbt-core
```

### 2. Comandos Principais do dbt
```bash
dbt debug    # Valida a conexão local
dbt deps     # Instala pacotes do dbt
dbt seed     # Carrega os dados estáticos
dbt run      # Executa as transformações
dbt test     # Roda os testes de qualidade
```