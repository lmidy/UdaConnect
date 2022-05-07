import os
from app.models import Location # noqa
from app.services import LocationService
from kafka import KafkaConsumer

# Kafka consumer initialization
TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
consumer = KafkaConsumer(TOPIC_NAME, bootstrap_servers=KAFKA_SERVER)

# Location consumer startup
print("Starting locations consumer...")
try:
    for message in consumer:
        print(message.value.decode('utf-8'))
        location: Location = LocationService.create(message.value.decode('utf-8'))
except KeyboardInterrupt:
    print("Stopping locations consumer...")
    consumer.close()
