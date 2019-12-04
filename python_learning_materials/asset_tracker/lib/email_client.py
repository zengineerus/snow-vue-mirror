import smtplib

from email.mime.text import MIMEText

class EmailClient:
    def __init__(self):
        self._from_address = 'do-not-reply@wwt.com'

    def send_email(self, to, subject, content):
        msg = MIMEText(content)

        msg['Subject'] = 'The contents of %s' % textfile
        msg['From'] = self._from_address
        msg['To'] = to

        s = smtplib.SMTP('smpt.wwt.com')
        s.sendmail(self._from_address, [to], msg.as_string())
        s.quit()

