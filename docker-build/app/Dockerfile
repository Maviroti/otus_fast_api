FROM python:3.12-slim

WORKDIR /app

# Чтобы выводил всё сразу а не через буфер
ENV PYTHONUNBUFFERED=1
# Чтобы писал не в байткоде 
ENV PYTHONDONTWRITEBYTECODE=1

# Устанавливаем Poetry
RUN pip install poetry

# Копируем файлы зависимостей сначала
COPY pyproject.toml poetry.lock* ./

# Устанавливаем зависимости (отключаем создание виртуального окружения)
RUN poetry config virtualenvs.create false && poetry install --no-root

# Копируем остальной код
COPY tasker-app ./
COPY docker-build/app/entrypoint.sh ./

ENV PATH="/app/.venv/bin:$PATH"

RUN chmod +x entrypoint.sh
ENTRYPOINT ["./entrypoint.sh"]

# CMD ["python", "app.py"]