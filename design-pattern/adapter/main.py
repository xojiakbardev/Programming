from notification import sms, telegram, email, NotificationSender


if __name__=="__main__":
    sms_service = sms.SMSService()
    sms_adapter = sms.SMSAdapter(sms_service)

    email_service = email.EmailService()
    email_adapter = email.EmailAdapter(email_service)

    telegram_service = telegram.TelegramService()
    telegram_adapter = telegram.TelegramAdapter(telegram_service)

    def notify(adapter:NotificationSender, receipt:str, message:str):
        adapter.send(receipt, message)

    notify(sms_adapter, "", "")
