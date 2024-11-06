import asyncio

import uvicorn
from fastapi import FastAPI

from app.tasks.handlers.handlers import router
from app.tasks.servires.tasks import task_worker

# create instance of the app
app = FastAPI()

# Connecting routes from other modules
app.include_router(router)

@app.on_event("startup")
async def startup_worker():
    asyncio.create_task(task_worker())


if __name__ == "__main__":
    # run app on the host and port
    uvicorn.run(app, host='localhost', port=2000)

