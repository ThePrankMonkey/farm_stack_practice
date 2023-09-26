FROM python:3.11-slim-bookworm

COPY . /usr/app

RUN pip install -r /usr/app/requirements-dev.txt

WORKDIR /usr/app/src

# ENTRYPOINT ["uvicorn", "main:app", "--reload", "--host", "0.0.0.0", "--port", "8000"]
