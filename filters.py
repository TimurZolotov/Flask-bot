from update_handlers import (
    get_message_text, 
    get_callback_data
)
from flask import request


def callback_data_filter(callback_data_value):
    def filter_decorator(func):
        def filter_wrapper(*args, **kwargs):
            if get_callback_data(request) in callback_data_value:
                func(*args, **kwargs)
        return filter_wrapper
    return filter_decorator

def message_text_filter(message_text):
    def filter_decorator(func):
        def filter_wrapper(*args, **kwargs):
            if get_message_text(request) in message_text:
                func(*args, **kwargs)
        return filter_wrapper
    return filter_decorator

def is_message_filter(func):
    def filter_wrapper(*args, **kwargs):
        if get_message_text(request):
            func(*args, **kwargs)
    return filter_wrapper
