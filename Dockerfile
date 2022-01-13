FROM python:3.9.9-slim
EXPOSE 5000/tcp
ADD . /app
WORKDIR /app
RUN pip install -r requirements.txt
RUN python app.py