FROM python:3.14.0a6-alpine3.21

RUN mkdir /app
WORKDIR /app

COPY . .

EXPOSE 4000

CMD [ "python3", "main.py" ]