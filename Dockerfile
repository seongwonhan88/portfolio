FROM python:3.6
ENV PYTHONUNBUFFERED 1

RUN mkdir /app
WORKDIR /app

RUN pip install -r requirements.txt
EXPOSE 8000

CMD exec gunicorn portfolio.wsgi:application -bind 0.0.0.0:8000 -workers 3
