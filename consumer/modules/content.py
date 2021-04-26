from typing import Dict

from database.client import Client


class ContentModule(dict):

    def __init__(self, database: Client):
        super().__init__()
        self.database = database

    def create(self, collection_name: str, content) -> Dict:
        collection = self.database.get_collection(collection_name)
        id = collection.insert_one(content).inserted_id
        content_created = collection.find_one({'_id': id})
        return content_created
