import smtplib
from email.mime.text import MIMEText
import sqlite3


def send_message(recipient: str, message: str) -> str:
    sender = "melnikov2007@list.ru"
    password = "PZ94AUbcFf4XQABq6sgx"
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


def get_email(database: str = "instance/new-flask.db") -> str:
    with sqlite3.connect(database=database) as connection:
        cursor = connection.cursor()
        cursor.execute(
            """
        SELECT email FROM post
        WHERE id = (SELECT MAX(id) FROM post);
            """)
        email = cursor.fetchall()
        return email[0][0]


def main():
    recipient = input()
    message = "Arulm0675:QhcVzvOG283yYq:silentfixxit41@gazeta.pl:oA5kFypaa2UtqGx"
    send_message(message=message, recipient=recipient)
    print(get_email())


if __name__ == "__main__":
    main()
