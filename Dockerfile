FROM ubuntu:18.04
RUN apt-get update && apt-get install -y \
    python3-pip \
    python3-dev
EXPOSE 5000
ADD . /app
WORKDIR /app
RUN python3 -m venv venv
RUN source venv\bin\activate
RUN pip install -r requirements.txt