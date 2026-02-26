import os
import motor.motor_asyncio
from pymongo import MongoClient
import datetime
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# MongoDB Connection String
MONGO_URI = os.getenv("MONGO_URI", "mongodb://localhost:27017")

# Async Client (for ASGI/Channels)
async_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_URI)
async_db = async_client['django_chat_db']
messages_collection_async = async_db['messages']

# Sync Client (for WSGI/Views)
sync_client = MongoClient(MONGO_URI)
sync_db = sync_client['django_chat_db']
messages_collection_sync = sync_db['messages']

async def save_message_async(user, message):
    """Saves a message to MongoDB asynchronously."""
    path = {
        "user": user,
        "message": message,
        "timestamp": datetime.datetime.now(datetime.UTC)
    }
    await messages_collection_async.insert_one(path)

def get_latest_messages_sync(limit=10):
    """Fetches latest messages from MongoDB synchronously."""
    messages = messages_collection_sync.find().sort("timestamp", -1).limit(limit)
    return list(messages)

def get_chat_thread_sync(user1, user2, limit=20):
    """Fetches full chat history between two specific users."""
    query = {
        "$or": [
            {"sender_id": user1, "receiver_id": user2},
            {"sender_id": user2, "receiver_id": user1}
        ]
    }
    messages = messages_collection_sync.find(query).sort("timestamp", 1).limit(limit)
    return list(messages)

def get_all_users_sync():
    """Fetches all unique users who have used the system (Contact List)."""
    users = messages_collection_sync.distinct("sender_id")
    return list(users)
