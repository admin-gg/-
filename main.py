def send_email(message, recipient, sender="university.help@gmail.com"):
    def is_valid_email(email):
        return "@" in email and (email.endswith(".com") or email.endswith(".ru") or email.endswith(".net"))

    if not is_valid_email(sender) or not is_valid_email(recipient):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}.")
        return

    if sender == recipient:
        print("Нельзя отправить письмо самому себе!")
        return

    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")

# Пример вызова функции
send_email("Текст сообщения", "user@example.com")  # Успешная отправка
send_email("Текст сообщения", "user@example.com", "user@example.com")  # Отправка самому себе
send_email("Текст сообщения", "invalid_email", "custom_sender@example.com")  # Неверный email


