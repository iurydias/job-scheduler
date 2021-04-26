import json

from flask import request

from jobs.shelf import Shelf
from broker.client import Broker
from json import dumps
import uuid


class JobHandler:

    def __init__(self, exchange_name: str, broker: Broker, shelf: Shelf):
        self.exchange_name = exchange_name
        self.broker = broker
        self.shelf = shelf

    def create(self):
        body = request.get_json()
        id = str(uuid.uuid4())
        job = {
            "id": id,
            "data": body
        }
        self.broker.publish(self.exchange_name, 'jobs.created_jobs', dumps(job))
        self.shelf.add_job(id)
        return job, 201

    def check(self):
        id = request.args.get("id", type=str)
        if not id:
            return {"id": "is missing"}, 400
        job_status = self.shelf.get_job_status(id)
        if not job_status:
            return {"id": "does not exist"}, 404
        return {"id": id, "status": job_status}, 200

    def handle(self, ch, method, properties, body):
        body_decoded = body.decode()
        id = json.loads(body_decoded)["id"]
        print("new finished job received: ", id)
        self.shelf.finish_job(id)
