import time

from dataclasses import dataclass


@dataclass
class TelegramService():
    def send_telegram(chat_id:str, msg:str):
        print("sending...")
        time.sleep(2)
        print(f"{msg} sent successfuly to {chat_id}")


@dataclass
class TelegramAdapter():
    service:TelegramService

    def send(self, chat_id:str, msg:str):
        self.service.send_telegram(chat_id, msg)
