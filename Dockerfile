# pull official base image
FROM python:3.11.4-slim-buster

# set work directory
WORKDIR ./

# copy project
COPY pyproject.toml poetry.lock ./

# Устанавливаем зависимости с помощью Poetry
RUN pip install poetry && poetry config virtualenvs.create false && poetry install --no-dev
RUN poetry install

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]