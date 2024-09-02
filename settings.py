"""File with settings and configs for the project"""

from envparse import Env

env = Env()

DATABASE_URL = env.str(
    "DATABASE_URL", default="postgresql+asyncpg://admin_queue:password@localhost:5432/task_queuing_new"
)
