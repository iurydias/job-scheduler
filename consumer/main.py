import sys, os
from broker.client import Broker
from database.client import Client as DatabaseClient
from database.config import Config as DBConfig
from handlers.content import ContentHandler
from modules.content import ContentModule


def run():
    db_config = DBConfig('mongo.service.com.br', 27017, "admin", "admin", "mydb")
    client = DatabaseClient(db_config)
    content_module = ContentModule(client)

    broker = Broker("rabbitmq.service.com.br", 5672)
    broker.declare_exchange("jobs", "direct")
    broker.declare_queue("finished_jobs")
    broker.bind_queue("finished_jobs", "jobs", "jobs.finished_jobs")
    broker.declare_queue("created_jobs")

    handler = ContentHandler(content_module, "content", broker)

    broker.set_consumer("created_jobs", handler.handle)
    broker.start_consume()


if __name__ == "__main__":
    try:
        run()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)
