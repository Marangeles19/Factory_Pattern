from notification import EmailNotification, SMSNotification, WhatsAppNotification

class NotificationFactory:
    @staticmethod
    def create_notification(channel: str):
        if channel == "email":
            return EmailNotification()
        elif channel == "sms":
            return SMSNotification()
        elif channel == "whatsapp":
            return WhatsAppNotification()
        else:
            raise ValueError(f"Can’t send notification via: {channel}")
