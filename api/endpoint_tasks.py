from fastapi import Depends, APIRouter
from sqlalchemy.ext.asyncio import AsyncSession

from database.models import Task
from database.sessions import get_db

router = APIRouter()


@router.post("/tasks/")
async def create_task(db: AsyncSession = Depends(get_db)):
    async with db.begin():
        task = Task(status="In Queue")
        db.add(task)
        await db.commit()
        return {"task_id": task.id}


@router.get("/tasks/{task_id}")
async def get_task_status(task_id: int, db: AsyncSession = Depends(get_db)):
    async with db.begin():
        task = await db.get(Task, task_id)
        if not task:
            return {'Error': "Task not found"}
        return {
            "status": task.status,
            "create_time": task.create_time,
            "start_time": task.start_time,
            "execute_to_time": task.execute_to_time,
        }
