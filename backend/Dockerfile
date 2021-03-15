# Образ системы основанный на Python 3.7
FROM python:3.7

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Директория внутри нашего контейнера. Она будет рабочей, т.е. там будет храниться наш код. 
WORKDIR /usr/src/backend

# Копируем файл зависимостей.
COPY ./req.txt /usr/src/req.txt
# Устанавливаем зависимости
RUN pip install -r /usr/src/req.txt

# Копируем проект в нашу папку в образе
COPY ./proxysite /usr/src/backend

# Открываем порт в контейнере для взаимодействия
EXPOSE 8000

# CMD [ "python", "manage.py", "runserver", "0.0.0.0:5000"]