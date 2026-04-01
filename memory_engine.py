# memory_engine.py

# This file stores conversation history
# so the AI can remember previous messages

conversation_history = []


def add_user_message(message):
    """
    Add user message to memory
    """
    conversation_history.append({
        "role": "user",
        "content": message
    })


def add_assistant_message(message):
    """
    Add assistant response to memory
    """
    conversation_history.append({
        "role": "assistant",
        "content": message
    })


def get_history():
    """
    Return conversation history
    """
    return conversation_history


def clear_memory():
    """
    Clear conversation history
    """
    global conversation_history
    conversation_history = []