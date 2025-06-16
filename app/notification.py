from abc import ABC, abstractmethod

# Interfaz
class Notification(ABC):
    @abstractmethod
    def send(self, message: str):
        pass

# Clases concretas
class EmailNotification(Notification):
    def send(self, message: str):
        print(f"[Email] {message}")

class SMSNotification(Notification):
    def send(self, message: str):
        print(f"[SMS] {message}")

class WhatsAppNotification(Notification):
    def send(self, message: str):
        print(f"[WhatsApp] {message}")
