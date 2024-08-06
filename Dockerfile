FROM python:3.9.19-slim


#не создавать файл с кэшом python
ENV PYTHONDONTWRITEDYTECODE 1
#не буфферизировать логи
ENV PYTHONUNBUFFERED 1


WORKDIR /app/backend

COPY ./requirements.txt /app/backend
RUN pip install --upgrade pip
RUN pip install -r /app/backend/requirements.txt
COPY . /app/backend