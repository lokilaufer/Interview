import email
import smtplib
import imaplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart


class EmailClient:
    def __init__(self, login, password, subject, recipients, message, header):
        self.login = login
        self.password = password
        self.subject = subject
        self.recipients = recipients
        self.message = message
        self.header = header
        self.gmail_smtp = "smtp.gmail.com"
        self.gmail_imap = "imap.gmail.com"

    def send_email(self):
        msg = MIMEMultipart()
        msg['From'] = self.login
        msg['To'] = ', '.join(self.recipients)
        msg['Subject'] = self.subject
        msg.attach(MIMEText(self.message))

        ms = smtplib.SMTP(self.gmail_smtp, 587)
        ms.ehlo()
        ms.starttls()
        ms.ehlo()

        ms.login(self.login, self.password)
        ms.sendmail(self.login, self.recipients, msg.as_string())
        ms.quit()

    def receive_email(self):
        mail = imaplib.IMAP4_SSL(self.gmail_imap)
        mail.login(self.login, self.password)
        mail.list()
        mail.select("inbox")
        criterion = '(HEADER Subject "%s")' % self.header if self.header else 'ALL'
        result, data = mail.uid('search', None, criterion)
        assert data[0], 'There are no letters with current header'
        latest_email_uid = data[0].split()[-1]
        result, data = mail.uid('fetch', latest_email_uid, '(RFC822)')
        raw_email = data[0][1]
        email_message = email.message_from_bytes(raw_email)
        mail.logout()


if __name__ == '__main__':
    email_client = EmailClient('login@gmail.com', 'qwerty', 'Subject', ['vasya@email.com', 'petya@email.com'],
                               'Message', None)
    email_client.send_email()
    email_client.receive_email()
