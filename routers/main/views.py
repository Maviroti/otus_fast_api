from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates

from routers.task.dependencies import GetTasksCRUD


router = APIRouter(tags=["main"])


templates = Jinja2Templates(directory="templates")


@router.get(
    "/",
    response_class=HTMLResponse,
    summary="Отображение главной страницы",
    description="Отображение страницы со списком всех задач",
)
async def index(request: Request, task_crud: GetTasksCRUD):
    """Выводим список тасок"""
    context = {
        "request": request,
        "active_page": "index",
        "tasks": task_crud.get_list(),
    }
    return templates.TemplateResponse("index.html", context)


@router.get(
    "/today",
    response_class=HTMLResponse,
    summary="Отображение страницы 'Сегодня'",
    description="Отображение страницы со списком задач у которых сегодня последний день",
)
async def today(request: Request, task_crud: GetTasksCRUD):
    """Выводим список задач у которых сегодня последний день"""
    today_tasks = task_crud.get_by_date()
    context = {
        "request": request,
        "active_page": "today",
        "tasks": today_tasks,
    }
    return templates.TemplateResponse("index.html", context)


@router.get(
    "/about/",
    summary="Отображение страницы 'О нac'",
    description="Отображение страницы с информацией о разработчике",
)
async def about(request: Request):
    """Выводим страницу about"""
    context = {
        "request": request,
        "active_page": "about",
    }
    return templates.TemplateResponse("about.html", context)
