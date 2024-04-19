FROM python:3.10.12

WORKDIR stockprediction

COPY requirements.txt requirements.txt

RUN pip install -r requirements.txt

COPY . .

CMD ["gunicorn", "-b", "0.0.0.0:3500", "-w", "1", "app:app"]
