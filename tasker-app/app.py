from fastapi import FastAPI
import uvicorn

from routers.task.views import router as task_router
from routers.main.views import router as main_router
from fastapi.staticfiles import StaticFiles


app = FastAPI()

# Монтируем статические файлы
app.mount("/static", StaticFiles(directory="static"), name="static")

app.include_router(main_router)
app.include_router(task_router)

if __name__ == "__main__":
    uvicorn.run("app:app", host="0.0.0.0", port=8000, reload=True)
