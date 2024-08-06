import logging

from pymongo.mongo_client import MongoClient

from backend.config.config import config

try:
    # Database session
    client = MongoClient(
        config.mongodb_config.construct_mongo_url()
    )
    logging.warning('Connect to mongodb successfully')

    # Database name
    db = client.messages_db

    # Database collection name
    collection_messages = db['messages']

except Exception as e:
    logging.error(f'Connect error {e}')
