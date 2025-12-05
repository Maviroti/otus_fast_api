from fastapi import APIRouter, HTTPException, Query
from schemas.task import task_list, TaskBaseSchema


router = APIRouter()


@router.get("/", response_model=list[TaskBaseSchema])
async def get_task(
    title: str = Query(
        None, description="Таски, которые содержат этот параметр в поле title"
    ),
    user: str = Query(
        None, description="Таски, которые содержат этот параметр в поле user"
    ),
    description: str = Query(
        None, description="Таски, которые содержат этот параметр в поле description"
    ),
):
    """Выводим список тасок"""
    result = []
    if title is not None:
        result = result + [task for task in task_list if title in task.title]
    if user is not None:
        result = result + [task for task in task_list if user in task.user]
    if description is not None:
        result = result + [
            task for task in task_list if description in task.description
        ]
    if not result:
        result = task_list
    return result


@router.get("/{task_id}/", response_model=TaskBaseSchema)
async def get_task_by_id(task_id: int):
    """Получаем таску по её id

    Args:
        task_id (int): id таски
    """
    if task_id < 0 or task_id > len(task_list) - 1:
        raise HTTPException(status_code=404, detail="Task not found")
    return task_list[task_id]


@router.post("/", response_model=TaskBaseSchema, status_code=201)
async def add_task(task: TaskBaseSchema):
    """добавляет таску"""
    task_list.append(task)
    return task


@router.put("/{task_id}/", response_model=TaskBaseSchema)
async def edit_task(task_id: int, task: TaskBaseSchema):
    """Изменяет таску по её ID"""
    if task_id < 0 or task_id > len(task_list) - 1:
        raise HTTPException(status_code=404, detail="Task not found")
    task_list[task_id] = task
    return task_list[task_id]


@router.delete("/{task_id}/")
async def del_task(task_id: int):
    """Удаляет таску по её ID"""
    if task_id < 0 or task_id > len(task_list) - 1:
        raise HTTPException(status_code=404, detail="Task not found")
    res = task_list.pop(task_id)
    return {"massage": f'Delete task "{res.title}"'}
