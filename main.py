# module_3_2
recipient= ('mr.fan63@yndex.ru')
sender= ('university.help@gmail.com')

def send_email(message: str, recipient: str, *, sender="university.help@gmail.com"):
    # Проверка на корректность e-mail отправителя и получателя
    if ("@" not in sender or not sender.endswith((".com", ".ru", ".net"))) or (
            "@" not in recipient or not recipient.endswith((".com", ".ru", ".net"))):
        print(f"Невозможно отправить письмо с адреса {sender} на адрес {recipient}")
        return

    # Проверка на отправку самому себе
    sender= ('mr.fan63@yndex.ru')
    recipient= ('mr.fan63@yndex.ru')

    if sender == recipient:

        print("Нельзя отправить письмо самому себе!")
        return

    # Проверка на отправителя по умолчанию
    if sender == "university.help@gmail.com":
        print(f"Письмо успешно отправлено с адреса {sender} на адрес {recipient}.")
    else:
        print(f"НЕСТАНДАРТНЫЙ ОТПРАВИТЕЛЬ! Письмо отправлено с адреса {sender} на адрес {recipient}.")



