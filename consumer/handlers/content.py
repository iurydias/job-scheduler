import json

from broker.client import Broker
from modules.content import ContentModule


class ContentHandler:

    def __init__(self, module: ContentModule, collection_name: str, broker: Broker):
        self.module = module
        self.collection_name = collection_name
        self.broker = broker

    def handle(self, ch, method, properties, body):
        body_decoded = body.decode()
        print("new message received: ", body_decoded)
        job = json.loads(body_decoded)
        self.module.create(self.collection_name, job["data"])
        self.broker.publish("jobs", "jobs.finished_jobs", body_decoded)
