from typing import Annotated, Optional
from collections.abc import Generator

from fastapi import Depends, Path, HTTPException, status
from sqlalchemy.orm import Session
from pydantic import PositiveInt

from routers.task.crud import TasksCRUD
from models import session_factory, Task


def get_session() -> Generator[Session]:
    """Зависимость для получения сессии БД"""
    with session_factory() as session:
        yield session


GetSession = Annotated[
    Session,
    Depends(get_session),
]


def get_tasks_crud(
    session: GetSession,
) -> TasksCRUD:
    """Фабрика для TasksCRUD"""
    return TasksCRUD(session)


GetTasksCRUD = Annotated[
    TasksCRUD,
    Depends(get_tasks_crud),
]


def get_task_by_id(
    task_id: Annotated[
        PositiveInt,
        Path(description="ID задачи", example=1),
    ],
    crud: GetTasksCRUD,
) -> Task:
    """Зависимость для получения задачи по ID"""
    task: Optional[Task] = crud.get_by_id(task_id)
    if task:
        return task

    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail=f"Task #{task_id} not found",
    )


GetTask = Annotated[
    Task,
    Depends(get_task_by_id),
]
