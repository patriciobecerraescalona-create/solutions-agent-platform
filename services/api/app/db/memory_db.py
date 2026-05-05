# Mock in-memory database

users = []
services = []
payments = []
whatsapp_outbox = []

def get_next_id(collection: list) -> int:
    return len(collection) + 1
