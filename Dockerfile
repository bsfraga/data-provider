FROM python:3.9.9-slim
EXPOSE 5000/tcp
ADD . /app
WORKDIR /app
RUN python -m venv venv
RUN source venv/bin/activate
RUN pip install -r requirements.txt