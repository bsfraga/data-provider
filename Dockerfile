FROM ubuntu:16.04
RUN apt-get update && apt-get install -y \
    apt-transport-https \
    ca-certificates \
    curl \
    software-properties-common \
    python3-pip \
    python3-dev
EXPOSE 5000
ADD . /app
WORKDIR /app
RUN pip3 install -r requirements.txt
CMD ["python3", "app.py"]