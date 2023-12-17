FROM python:3.10.5

WORKDIR /usr/src/app
ENV FLASK_APP=run.py

COPY /app/requirements.txt ./

RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt