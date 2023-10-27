import smtplib
from email.mime.text import MIMEText


def send_message(recipient: str, message: str) -> str:
    sender = "melnikov2007@list.ru"
    password = "tvTMhCkbvPd4kxZwiHwN"
    server = smtplib.SMTP('smtp.mail.ru', 587)
    server.starttls()

    try:
        server.login(sender, password)
        msg = MIMEText(message)
        msg["Subject"] = "Ваш аккаунт"
        server.sendmail(sender, recipient, f"Subject: Your account from Fastdobeg store\n{msg}")
        return "success"
    except Exception as _ex:
        return f"error: {_ex}\nCheck email or pass"


def main():
    recipient = input()
    message = "Arulm0675:QhcVzvOG283yYq:silentfixxit41@gazeta.pl:oA5kFypaa2UtqGx"
    send_message(message=message, recipient=recipient)


if __name__ == "__main__":
    main()
