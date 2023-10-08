import smtplib
from email.mime.text import MIMEText


def send_message(message):
    sender = "melnikov2007@list.ru"
    password = "tvTMhCkbvPd4kxZwiHwN"
    # recipient = ""
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Ваш аккаунт!"
        server.sendmail(sender, sender, f"Subject: Your account from Fastdobeg store\n{msg}")
        return "success"
    except Exception as _ex:
        return f"error: {_ex}\nCheck email or pass"


def main():
    message = input("write message ")
    print(send_message(message=message))


if __name__ == "__main__":
    main()
