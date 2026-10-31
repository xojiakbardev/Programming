import time

from dataclasses import dataclass


@dataclass
class EmailService():
    def send_email(email:str, sms:str):
        print("sending...")
        time.sleep(2)
        print(f"{sms} sent successfuly to {email}")


@dataclass
class EmailAdapter():
    service: EmailService

    def send(self, receipt:str, sms:str):
        self.service.send_email(receipt, sms)
