user_memory_store = {}

def get_memory_for_user(memory_id):
    if memory_id not in user_memory_store:
        user_memory_store[memory_id] = [
            {"role": "system", "content": "You are a helpful assistant."}
        ]
    return user_memory_store[memory_id]