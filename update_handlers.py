def get_chat_id(data):
    try:
        if "message" in data.json:
            return data.json["message"]["chat"]["id"]
        elif "callback_query" in data.json:
            return data.json["callback_query"]["message"]["chat"]["id"]
    except KeyError:
        print("Some key from get_chat_id function not found in update")

def get_callback_data(data):
    try:
        if "callback_query" in data.json:
            return data.json["callback_query"]["data"]
    except KeyError:
        print("Some key from get_callback_data function not found in update")

def get_message_text(data):
    try:
        if "message" in data.json:
            return data.json["message"]["text"]
    except KeyError:
        print("Some key from get_message_text function not found in update")
