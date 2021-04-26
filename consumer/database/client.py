from pymongo import MongoClient, collection

from database.config import Config


class Client:
    def __init__(self, config: Config):
        self.client = MongoClient(config.host, config.port, username=config.user, password=config.password)
        self.database = self.client[config.database]

    def get_collection(self, name: str) -> collection:
        return self.database[name]

    def close(self):
        self.client.close()
