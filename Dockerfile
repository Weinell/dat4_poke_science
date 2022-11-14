FROM python:alpine

WORKDIR /app

RUN pip install poetry==1.2.2
RUN python3 -m venv /venv

COPY pyproject.toml poetry.lock ./

COPY . .

CMD ["python3", "main.py"]
