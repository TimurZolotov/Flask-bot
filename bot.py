from singleton import Singleton
import requests


class Bot(Singleton):
    def __init__(self, token):
        self.__token = token

    def send_message(self, chat_id, text, reply_markup=None):
        method = "sendMessage"
        url = f"https://api.telegram.org/bot{self.__token}/{method}"
        data = {"chat_id": chat_id, "text": text, "reply_markup": reply_markup}
        requests.post(url, data)

    def send_photo(self, chat_id, photo_url, caption=None, reply_markup=None):
        method = "sendPhoto"
        url = f"https://api.telegram.org/bot{self.__token}/{method}"
        data = {"chat_id": chat_id, "photo": photo_url, "reply_markup": reply_markup, "caption": caption}
        requests.post(url, data)

    def send_document(self, chat_id, document, caption=None):
        method = "sendDocument"
        url = f"https://api.telegram.org/bot{self.__token}/{method}"
        data = {"chat_id": chat_id, "caption": caption}
        requests.post(url, data, files={"document": document})
