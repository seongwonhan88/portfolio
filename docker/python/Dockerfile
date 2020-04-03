FROM python:3.6
MAINTAINER seongwonhan88@localhost

ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

COPY docker/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]



#CMD bash -c "python manage.py makemigrations && python manage.py migrate && gunicorn portfolio.wsgi --bind 0.0.0.0:8000"