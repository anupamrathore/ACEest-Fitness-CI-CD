# Use official Python slim
FROM python:3.11-slim

# set workdir
WORKDIR /app

# avoid Python writing .pyc files
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# copy requirements first (cache)
COPY requirements.txt .

# install dependencies
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

# copy application code
COPY . .

# expose port used by the app
EXPOSE 5000

# run with gunicorn (wsgi:app points to wsgi.py -> app)
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "wsgi:app", "--workers", "2", "--timeout", "120"]
