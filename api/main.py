import threading

from flask import Flask

import sys, os
from jobs.handler import JobHandler
from jobs.shelf import Shelf
from broker.client import Broker

app = Flask(__name__)

app_broker = Broker("rabbitmq.service.com.br", 5672)
app_broker.declare_exchange("jobs", "direct")
app_broker.declare_queue("created_jobs")
app_broker.bind_queue("created_jobs", "jobs", "jobs.created_jobs")

thread_broker = Broker("rabbitmq.service.com.br", 5672)
thread_broker.declare_queue("finished_jobs")

job_shelf = Shelf()
job_handler = JobHandler("jobs", app_broker, job_shelf)

thread_broker.set_consumer("finished_jobs", job_handler.handle)


@app.route("/job/create", methods=["POST"])
def create_job():
    return job_handler.create()


@app.route("/job", methods=["GET"])
def check_job():
    return job_handler.check()


if __name__ == "__main__":
    try:
        threading.Thread(target=thread_broker.start_consume).start()
        app.run(host="0.0.0.0")
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
