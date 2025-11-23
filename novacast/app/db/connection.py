from motor.motor_asyncio import AsyncIOMotorClient
from pymongo import errors
import os
import asyncio

class DatabaseConnection:
    def __init__(self, uri: str, db_name: str):
        self.client = AsyncIOMotorClient(uri)
        self.db = self.client[db_name]

    async def close(self):
        self.client.close()

    async def get_collection(self, collection_name: str):
        try:
            return self.db[collection_name]
        except errors.PyMongoError as e:
            print(f"Error accessing collection {collection_name}: {e}")
            return None

async def init_db():
    db_uri = os.getenv("DATABASE_URI", "mongodb://localhost:27017")
    db_name = os.getenv("DATABASE_NAME", "novacast")
    db_connection = DatabaseConnection(db_uri, db_name)
    return db_connection

# Example usage
if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    db = loop.run_until_complete(init_db())
    # Perform database operations here
    loop.run_until_complete(db.close())