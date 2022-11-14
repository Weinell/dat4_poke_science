FROM python:alpine

WORKDIR /app

RUN pip install poetry==1.2.2
RUN python3 -m venv /venv

COPY pyproject.toml poetry.lock ./
RUN poetry export -f requirements.txt | /venv/bin/pip install -r /dev/stdin

COPY . .
RUN poetry build && /venv/bin/pip install dist/*.whl

CMD ["python3", "main.py"]
