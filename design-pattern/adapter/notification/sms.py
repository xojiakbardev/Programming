import time

from dataclasses import dataclass


@dataclass
class SMSService():
    def send_sms(phone:str, sms:str):
        print("sending...")
        time.sleep(2)
        print(f"{sms} sent successfuly to {phone}")


@dataclass
class SMSAdapter():
    service: SMSService

    def send(self, receipt:str, sms:str):
        self.service.send_sms(receipt, sms)
