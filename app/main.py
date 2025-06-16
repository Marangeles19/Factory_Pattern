from notification_factory import NotificationFactory

def main():
    print("=== Notificación Factory ===")
    channel = input("¿Qué canal deseas usar? (email/sms/whatsapp): ").lower()

    try:
        notification = NotificationFactory.create_notification(channel)
        notification.send("Hola! Este es un mensaje de prueba.")
    except ValueError as e:
        print(e)

if __name__ == "__main__":
    main()
