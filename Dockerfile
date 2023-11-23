FROM python:3.10

ADD searchEngineApi.py .
ADD requirements.txt .
ADD consumer.py .

RUN pip install -r requirements.txt

EXPOSE 6969