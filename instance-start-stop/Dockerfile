FROM python:3.8.2-slim-buster

RUN mkdir /app_run
WORKDIR /app_run
COPY requirements.txt /app_run/requirements.txt
RUN python -m pip install --upgrade pip
RUN python -m pip install -r requirements.txt
COPY /app /app_run/app
COPY ./main.py /app_run/main.py
CMD ["python", "/app_run/main.py"]