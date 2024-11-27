# Web service for organizing a task queue

<br>

## Contents
- [Functionality](#functionality)
- [Technology](#technology)
- [Application startup](#application-startup)
- [Deploy application](#deploy-application)

<br>

## Functionality
  - API-endpoint that, when accessed, creates a task, adds it to the queue, and returns the task number to the user;
  - API-endpoint returns task status in json format {'status': '...', 'create_time': '...', 'start_time': '...', 'time_to_execute': '...'}.

## Technology

<details><summary>List</summary>

**Programming languages:**

[![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)](https://www.python.org/)

**Framework:**

[![FastAPI](https://img.shields.io/badge/FastAPI-v0.112.2-blue?logo=FastAPI)](https://fastapi.tiangolo.com/)

**Databases:**

[![PostgreSQL](https://img.shields.io/badge/-PostgreSQL-464646?logo=PostgreSQL)](https://www.postgresql.org/)

</details>

## Application startup

```bash
git clone https://github.com/Ilya-kutylev/task_queuing.git
cd task-queuing-fastapi
```
- Activation of the virtual environment and install dependencies:
```bash
.venv/Scripts/activate
python -m pip install -r requirements.txt
```
- First migrations and server startup:
```bash
alembic upgrade head
uvicorn main:app --host localhost --port 2000
```
To test API endpoints, the Swagger tool is used at http://localhost:2000/docs

## Deploy application
```bash
docker compose up --build
docker compose down
```
