FROM python:3.10.12

WORKDIR stockprediction

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "app.py" ]

