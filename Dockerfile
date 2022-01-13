FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-venv \
    python3-dev
EXPOSE 5000
ADD . /app
WORKDIR /app
RUN source venv\bin\activate
RUN pip install -r requirements.txt