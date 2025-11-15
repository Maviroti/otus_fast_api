from pydantic import BaseModel


class Task(BaseModel):
    title: str
    user: str
    description: str
    end_time: str


task_list = [
    Task(
        title='Разработка FastAPI приложения',
        user='Вася Иванов',
        description='Разработать приложение по данным из урока',
        end_time="12.11.2025",
    ),
    Task(
        title='Code-rev',
        user='Антон Антонов',
        description='Проверить код FastAPI приложения',
        end_time="13.11.2025",
    ),
    Task(
        title='Тестирование FastAPI приложения',
        user='Иван Первый',
        description='Проверить работу приложения и завести баги',
        end_time="14.11.2025",
    ),
    Task(
        title='Подготовка требований для FastAPI приложения версии 2.0',
        user='Кирилл Котов',
        description='Написать требования ко второй версии приложения, с учётом новых фич',
        end_time="15.11.2025",
    )
]
