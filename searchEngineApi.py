from fastapi import FastAPI, Path
from pydantic import BaseModel

app = FastAPI()

pages = {
    1: {
        "name": "dummy-page",
        "page_url": "dummyurl.com",
        "text_body": "some random information",
        "size": 1200
    }
}

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

@app.get("/ingest")
def ingest_page():
    return {"Message": "I'm ingesting ..."}