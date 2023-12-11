FROM python:3.9-slim

RUN mkdir /app

COPY requirements.txt /app

RUN pip3 install -r /app/requirements.txt --no-cache-dir

COPY cats_blog/ /app

WORKDIR /app

CMD ["gunicorn", "cats_blog.wsgi:application", "--bind", "0:8000" ]