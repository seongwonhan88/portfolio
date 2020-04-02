FROM python:3.6
MAINTAINER seongwonhan88@localhost

ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

CMD ["python", "manage.py", "makemigrations"]
CMD ["python", "manage.py", "migrate"]
CMD ["gunicorn", "portfolio.wsgi", "--bind", "0.0.0.0:8000"]