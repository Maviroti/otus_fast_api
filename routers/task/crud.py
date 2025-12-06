from datetime import date
import logging
from typing import Optional
from sqlalchemy import func, select
from sqlalchemy.orm import Session

from models.task import Task
from schemas.task import TaskCreateSchema, TaskUpdateSchema

log = logging.getLogger(__name__)


class TasksCRUD:
    def __init__(self, session: Session):
        self.session = session

    def create(self, task_create: TaskCreateSchema) -> Task:
        """Создать новую задачу"""
        task = Task(
            title=task_create.title,
            user_name=task_create.user_name,
            body=task_create.body,
            end_date=task_create.end_date,
        )
        self.session.add(task)
        self.session.commit()
        self.session.refresh(task)
        log.info(f"Created task #{task.id}")
        return task

    def get_by_id(self, task_id: int) -> Optional[Task]:
        """Получить задачу по ID"""
        return self.session.get(Task, task_id)

    def get_list(self) -> list[Task]:
        """Получить список задач"""
        statement = select(Task).order_by(Task.id)
        result = self.session.scalars(statement)
        return list(result.all())

    def update(self, task_id: int, task_update: TaskUpdateSchema) -> Optional[Task]:
        """Обновить задачу"""
        task = self.get_by_id(task_id)
        if not task:
            return None

        update_data = task_update.model_dump(exclude_unset=True)
        for key, value in update_data.items():
            setattr(task, key, value)

        self.session.commit()
        self.session.refresh(task)
        log.info(f"Updated task #{task.id}")
        return task

    def delete(self, task_id: int) -> bool:
        """Удалить задачу"""
        task = self.get_by_id(task_id)
        if not task:
            return False

        self.session.delete(task)
        self.session.commit()
        log.info(f"Deleted task #{task_id}")
        return True

    def get_by_date(
        self,
        target_date: date = date.today(),
    ) -> list[Task]:
        """Получить задачи по конкретной дате"""
        statement = (
            select(Task)
            .where(func.date(Task.end_date) == target_date)
            .order_by(Task.id)
        )

        result = self.session.scalars(statement)
        return list(result.all())
