FROM python:alpine

WORKDIR /app

RUN pip3 install poetry==1.2.2

COPY pyproject.toml poetry.lock ./

COPY . .

CMD ["python3", "src/main.py"]
