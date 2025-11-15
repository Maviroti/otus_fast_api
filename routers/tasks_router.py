from datetime import datetime
from fastapi import APIRouter, HTTPException, Query, Request, Form
from models import task_list, Task
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse, RedirectResponse


router = APIRouter()
templates = Jinja2Templates(directory="templates")


@router.get("/tasks/{task_id}/", response_class=HTMLResponse)
async def get_task_by_id(request: Request, task_id: int):
    """Получаем таску по её id"""
    if task_id < 0 or task_id > len(task_list) - 1:
        raise HTTPException(status_code=404, detail="Task not found")
    context = {
        "request": request,
        "task": task_list[task_id],
    }
    return templates.TemplateResponse("task.html", context)


@router.get("/add_task/", response_class=HTMLResponse)
async def add_form(request: Request):
    """Открываем форму создания задачи"""
    context = {
        "request": request,
    }
    return templates.TemplateResponse("add_task_form.html", context)


@router.post("/add_task/", response_class=RedirectResponse)
async def add_task(
    user: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    end_time: str = Form(...)
):
    """Создаёт таску ии переносит на страницу этой таски"""
    # Преобразуем дату из гггг-мм-дд в дд.мм.гггг
    formatted_date = convert_time_format(end_time)
    # Создаем задачу
    task = Task(
        user=user,
        title=title,
        description=description,
        end_time=formatted_date
    )
    task_list.append(task)
    new_task_id = task_list.index(task)
    return RedirectResponse(
        url=f"/tasks/{new_task_id}/",
        status_code=303
    )


@router.get("/edit_task/{task_id}/", response_class=HTMLResponse)
async def edit_task_form(request: Request, task_id: int):
    """Открываем форму для редактирования задачи"""
    if task_id < 0 or task_id > len(task_list) - 1:
        raise HTTPException(status_code=404, detail="Task not found")
    context = {
        "request": request,
        "task": task_list[task_id],
        "task_id": task_id,
    }
    return templates.TemplateResponse("edit_task.html", context)


@router.post("/edit_task/{task_id}/", response_class=RedirectResponse)
async def edit_task(
    task_id: int,
    user: str = Form(...),
    title: str = Form(...),
    description: str = Form(...),
    end_time: str = Form(...)
):
    """Редактируем задачу"""
    if task_id < 0 or task_id > len(task_list) - 1:
        raise HTTPException(status_code=404, detail="Task not found")
    # Преобразуем дату из гггг-мм-дд в дд.мм.гггг
    formatted_date = convert_time_format(end_time)
    # Создаем задачу
    task = Task(
        user=user,
        title=title,
        description=description,
        end_time=formatted_date
    )
    task_list[task_id] = task
    return RedirectResponse(
        url=f"/tasks/{task_id}/",
        status_code=303
    )


@router.delete("/del_task/{task_id}")
async def delete_task(task_id: int):
    """Метод для удаления задачи"""
    if 0 <= task_id < len(task_list):
        del task_list[task_id]
        return {"message": "Task deleted successfully"}
    raise HTTPException(status_code=404, detail="Task not found")


def convert_time_format(time: str) -> str:
    """Конвертирует формат времени"""
    # Преобразуем дату из гггг-мм-дд в дд.мм.гггг
    if '-' in time:
        date_obj = datetime.strptime(time, "%Y-%m-%d")
        formatted_date = date_obj.strftime("%d.%m.%Y")
    else:
        date_obj = datetime.strptime(time, "%d.%m.%Y")
        formatted_date = date_obj.strftime("%Y-%m-%d")
    return formatted_date


# Назначаем фильтр для jinja2
templates.env.filters["convert_time_format"] = convert_time_format
