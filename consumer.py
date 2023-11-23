from kafka import KafkaConsumer

consumer = KafkaConsumer('baeldung', bootstrap_servers=['kafka:9092'])
for msg in consumer:
    print(msg.value)