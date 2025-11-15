from fastapi import FastAPI
import uvicorn
from routers.main_router import router as main_router
from routers.tasks_router import router as tasks_router
from routers.api_tasks_router import router as api_tasks_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Монтируем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main_router, tags=['main'])
app.include_router(tasks_router, tags=['tasks'])
app.include_router(api_tasks_router, prefix="/api/tasks", tags=['api tasks'])

if __name__ == "__main__":
    uvicorn.run("app:app", host="127.0.0.1", port=8123, reload=True)
