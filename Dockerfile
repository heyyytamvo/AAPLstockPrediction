FROM python:3.10.12

WORKDIR stockprediction

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "127.0.0.1:3500", "-w", "1", "app:app"]
