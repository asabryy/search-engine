FROM python:3.10

ADD searchEngineApi.py .
ADD requirements.txt .
ADD consumer.py .

RUN pip install -r requirements.txt

CMD ["uvicorn","searchEngineApi:app", "--reload", "--host", "0.0.0.0"]