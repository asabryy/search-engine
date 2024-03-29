from fastapi import FastAPI, Path
from pydantic import BaseModel
from kafka import KafkaProducer, KafkaConsumer
import json

app = FastAPI()
producer = KafkaProducer(bootstrap_servers=['kafka:9092'], api_version=(1, 1, 0))
consumer = KafkaConsumer('baeldung', bootstrap_servers=['kafka:9092'],api_version=(1, 1, 0))

pages = {
    1: {
        "name": "dummy-page",
        "page_url": "dummyurl.com",
        "text_body": "some random information",
        "size": 1200
    }
}


class Document(BaseModel):
    document: str
   
    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, 
            sort_keys=True, indent=4)


@app.get("/")
def index():
    return {"system": "Frontend"}

@app.get("/query")
def query_db():
    return {"Messasge": "I'm querying"}

@app.post("/ingest")
def ingest_document(document: Document):
    print(f"Received document is: {document}")
    producer.send('baeldung', value=document.toJSON().encode('utf-8'))
    producer.flush()
    return {"Message": "I'm ingesting ..."}

@app.get("/consume")
def consume():
    for msg in consumer:
        print(f'Consumed Message: {msg.value}')