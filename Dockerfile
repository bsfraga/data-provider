FROM python:3.9.9-slim
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python app.py