from fastapi import APIRouter, Request, Query
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from schemas.task import task_list, TaskBaseSchema
from datetime import date


router = APIRouter()


templates = Jinja2Templates(directory="templates")


@router.get("/", response_class=HTMLResponse)
async def index(request: Request):
    """Выводим список тасок"""
    context = {
        "request": request,
        "active_page": "index",
        "tasks": task_list,
    }
    return templates.TemplateResponse("index.html", context)


@router.get("/today", response_class=HTMLResponse)
async def today(request: Request):
    """Выводим список задач у которых сегодня последний день"""
    res = task_list
    today = date.today().strftime("%d.%m.%Y")
    res = [task for task in task_list if task.end_time == today]
    context = {
        "request": request,
        "active_page": "today",
        "tasks": res,
    }
    return templates.TemplateResponse("index.html", context)


@router.get("/about/")
async def about(request: Request):
    """Выводим страницу about"""
    context = {
        "request": request,
        "active_page": "about",
    }
    return templates.TemplateResponse("about.html", context)
