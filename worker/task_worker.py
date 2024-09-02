import asyncio
import random
from datetime import datetime

from sqlalchemy import text
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Task
from database.sessions import async_session

semaphore = asyncio.Semaphore(2)


async def process_task(task_id: int, db: AsyncSession):
    async with db.begin():
        task = await db.get(Task, task_id)
        task.status = "Run"
        task.start_time = datetime.now()
        await db.commit()

    exec_time = random.randint(0, 10)
    await asyncio.sleep(exec_time)

    async with db.begin():
        task.status = "Completed"
        task.execute_to_time = exec_time
        await db.commit()


async def task_worker():
    while True:
        async with async_session() as session:
            tasks = await session.execute(text("SELECT id FROM tasks WHERE status = 'In Queue' ORDER BY id"))
            tasks_to_process = tasks.scalars().all()

            # Wait for an available slot at the semaphore and start the task
            for task_id in tasks_to_process:
                await semaphore.acquire()
                asyncio.create_task(run_task_with_semaphore(task_id))

        await asyncio.sleep(1)


async def run_task_with_semaphore(task_id: int):
    try:
        async with async_session() as session:
            await process_task(task_id, session)
    finally:
        semaphore.release()
