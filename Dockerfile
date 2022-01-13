from python:latest

WORKDIR /app

COPY . /app
RUN pip3 install -r requirements.txt

COPY . .

CMD [ "python3 app.py" ] 