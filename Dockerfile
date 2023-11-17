FROM python:3.10

ADD searchEngineApi.py .
ADD requirements.txt .

RUN pip install -r requirements.txt

CMD ["python", "./searchEngineApi.py"]