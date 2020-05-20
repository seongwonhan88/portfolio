FROM python:3.6

ENV PYTHONUNBUFFERED 1

COPY . /app
WORKDIR /app

RUN pip install -r requirements/prod.txt

COPY docker/prod/python/entrypoint.sh /entrypoint.sh

RUN chmod +x /entrypoint.sh
ENTRYPOINT ["/entrypoint.sh"]



#CMD bash -c "python manage.py makemigrations && python maneage.py migrate && gunicorn portfolio.wsgi --bind 0.0.0.0:8000"