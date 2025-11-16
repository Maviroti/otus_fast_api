FROM python:3.12-slim

WORKDIR /app

# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы зависимостей сначала
COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости (отключаем создание виртуального окружения)
RUN poetry config virtualenvs.create false && poetry install --no-root

# Копируем остальной код
COPY . .

CMD ["python", "app.py"]