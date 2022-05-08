import time
import json
from concurrent import futures

import grpc
import os
import location_pb2
import location_pb2_grpc
import logging

from kafka import KafkaProducer

TOPIC_NAME = os.environ["TOPIC_NAME"]
KAFKA_SERVER = os.environ["KAFKA_SERVER"]
producer = KafkaProducer(bootstrap_servers=KAFKA_SERVER)


class LocationServicer(location_pb2_grpc.LocationServiceServicer):
    def Create(self, request, context):
        request_value = {
            "person_id": request.person_id,
            "latitude": request.latitude,
            "longitude": request.longitude,
            "created_at": request.created_at
        }
        logging.info("Received a message")
        print(request_value)
        logging.info("request_value ==> {}".format(request_value))
        kafka_data = json.dumps(request_value).encode()
        producer.send(TOPIC_NAME, kafka_data)
        producer.flush()

        return location_pb2.LocationMessage(**request_value)


# Initialize gRPC server
server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()
# Keep thread alive
try:
    while True:
        time.sleep(86400)
except KeyboardInterrupt:
    server.stop(0)
