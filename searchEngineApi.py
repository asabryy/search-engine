from fastapi import FastAPI, Path
from pydantic import BaseModel
from kafka import KafkaProducer

app = FastAPI()
producer = KafkaProducer(bootstrap_servers='kafka:9092')


pages = {
    1: {
        "name": "dummy-page",
        "page_url": "dummyurl.com",
        "text_body": "some random information",
        "size": 1200
    }
}

producer.send('baeldung', b'(1, Main Menu), (2, Phone) , (3, Smart Phone), (4, iPhone)')


class Page(BaseModel):
    name: str
    page_url: str
    text_body: str
    size: int


@app.get("/")
def index():
    return {"system": "Frontend"}

@app.get("/query")
def query_db():
    return {"Messasge": "I'm querying"}

@app.post("/ingest")
def ingest_page():
    return {"Message": "I'm ingesting ..."}