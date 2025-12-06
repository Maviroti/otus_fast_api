from datetime import datetime

from fastapi import APIRouter, Form, HTTPException, Request
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates

from routers.task.dependencies import GetTasksCRUD

from models.task import Task
from schemas.task import TaskCreateSchema, TaskUpdateSchema
from routers.task.dependencies import GetTasksCRUD


router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


templates = Jinja2Templates(directory="templates")


@router.get(
    "/add/",
    response_class=HTMLResponse,
    summary="Открыть страницу с формой создания задачи",
    description="Открывает страницу с формой создания задачи",
)
async def add_form(request: Request):
    """Открываем форму создания задачи"""
    context = {
        "request": request,
    }
    return templates.TemplateResponse("add_task_form.html", context)


@router.post(
    "/add/",
    response_class=RedirectResponse,
    summary="Создать задачу",
    description="Создаёт таску и переносит на страницу этой таски",
)
async def add_task(
    crud: GetTasksCRUD,
    user: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    end_time: str = Form(...),
):
    """Создаёт таску и переносит на страницу этой таски"""
    task = TaskCreateSchema(
        title=title,
        user_name=user,
        body=description,
        end_date=datetime.strptime(end_time, "%Y-%m-%d"),
    )
    new_task = crud.create(task)
    return RedirectResponse(url=f"/tasks/{new_task.id}/", status_code=303)


@router.get(
    "/{task_id}/",
    response_class=HTMLResponse,
    summary="Открыть страницу задачи",
    description="Открывает страницу задачи",
)
async def get_task_by_id(
    request: Request,
    task_id: int,
    crud: GetTasksCRUD,
):
    """Получаем таску по её id"""
    task = crud.get_by_id(task_id)
    context = {
        "request": request,
        "task": task,
    }
    return templates.TemplateResponse("task.html", context)


@router.get(
    "/edit/{task_id}/",
    response_class=HTMLResponse,
    summary="Открыть страницу редактирования задачи",
    description="Открывает страницу с формой для редактирования задачи",
)
async def edit_task_form(
    request: Request,
    task_id: int,
    crud: GetTasksCRUD,
):
    """Открываем форму для редактирования задачи"""
    task = crud.get_by_id(task_id)
    if task is None:
        raise HTTPException(status_code=404, detail="Task not found")

    context = {
        "request": request,
        "task": task,
        "task_id": task_id,
    }
    return templates.TemplateResponse("edit_task.html", context)


@router.post(
    "/edit/{task_id}/",
    response_class=RedirectResponse,
    summary="Редактировать задачу",
    description="Редактирует задачу",
)
async def edit_task(
    crud: GetTasksCRUD,
    task_id: int,
    user_name: str = Form(...),
    title: str = Form(...),
    body: str = Form(...),
    end_date: str = Form(...),
):
    """Редактируем задачу"""
    task = TaskUpdateSchema(
        user_name=user_name,
        title=title,
        body=body,
        end_date=datetime.strptime(end_date, "%Y-%m-%d"),
    )
    crud.update(task_id, task)
    return RedirectResponse(url=f"/tasks/{task_id}/", status_code=303)


@router.delete("/del/{task_id}")
async def delete_task(
    task_id: int,
    crud: GetTasksCRUD,
    summary="Удалить задачу",
    description="Удаляет задачу",
):
    """Метод для удаления задачи"""
    crud.delete(task_id)
    return {"message": "Task deleted successfully"}
