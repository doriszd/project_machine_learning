FROM python:3.7.9

WORKDIR /usr/src/app

COPY requirements.txt ./

RUN pip install --no-cache-dir -r requirements.txt

COPY . .

ENV FLASK_APP=server.py

CMD flask run --host=0.0.0.0