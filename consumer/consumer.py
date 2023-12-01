from kafka import KafkaConsumer
from fastapi import FastAPI

consumer = KafkaConsumer('baeldung', bootstrap_servers=['kafka:9092'],api_version=(1, 1, 0))
app = FastAPI()

@app.get("/")
def index():
    return {"consumer": "up"}

@app.post("/")
def print_msg():
    for msg in consumer:
        print(msg.value)