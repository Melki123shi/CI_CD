FROM python:3.14.0a6-alpine3.21

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "main.py" ]