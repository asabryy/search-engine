from fastapi import FastAPI, Path
from pydantic import BaseModel
from kafka import KafkaProducer
import json

app = FastAPI()
producer = KafkaProducer(bootstrap_servers=['kafka:9092'], api_version=(1, 1, 0))


pages = {
    1: {
        "name": "dummy-page",
        "page_url": "dummyurl.com",
        "text_body": "some random information",
        "size": 1200
    }
}


class Document(BaseModel):
    documnet: str


@app.get("/")
def index():
    return {"system": "Frontend"}

@app.get("/query")
def query_db():
    return {"Messasge": "I'm querying"}

@app.post("/ingest")
def ingest_document(document: Document):
    print(f"Received document is: {document}")
    producer.send('baeldung', value=json.dumps(document).encode('utf-8'))
    producer.flush()
    return {"Message": "I'm ingesting ..."}