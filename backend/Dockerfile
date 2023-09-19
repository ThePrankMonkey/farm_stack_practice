FROM python:3.11-slim-bookworm

WORKDIR /usr/app

COPY . /usr/app

# ENTRYPOINT ["tail", "-f", "/dev/null"]

RUN pip install -r requirements-dev.txt

WORKDIR /usr/app/src

# ENTRYPOINT ["tail", "-f", "/dev/null"]
ENTRYPOINT ["uvicorn", "main:app", "--reload"]