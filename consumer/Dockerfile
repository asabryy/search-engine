FROM python:3.10

ADD consumer.py .
add requirements.txt .

RUN pip install -r requirements.txt

CMD ["uvicorn","consumer:app", "--reload", "--host", "0.0.0.0"]