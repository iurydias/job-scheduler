import pika


class Broker:
    def __init__(self, host: str, port: int):
        self.connection = pika.BlockingConnection(pika.ConnectionParameters(host, port))
        self.channel = self.connection.channel()

    def declare_exchange(self, name: str, exchange_type: str):
        self.channel.exchange_declare(name, exchange_type)

    def bind_queue(self, queue: str, exchange: str, binding_key: str):
        self.channel.queue_bind(queue, exchange, binding_key)

    def declare_queue(self, name: str):
        self.channel.queue_declare(name)

    def set_consumer(self, queue: str, callback):
        self.channel.basic_consume(queue, callback, auto_ack=True)

    def start_consume(self):
        print("Starting consuming...")
        self.channel.start_consuming()

    def publish(self, exchange: str, routing_key: str, body: bytes):
        self.channel.basic_publish(exchange, routing_key, body)

    def close(self):
        self.connection.close()
