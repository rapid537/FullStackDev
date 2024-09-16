import smtplib
from email.message import EmailMessage

from bartend import app
from bartend import BASE_CONFIG
from dev.dev_tools import key_generator


class AuthEmail:
    def __init__(self):
        self.email_address = None
        self.confirmation_code = None

    def send_confirm_code(self, email_address=None):
        self.confirmation_code = key_generator(6)
        self.email_address = email_address

        content = f"""
            Account Confirmation Code:

            {self.confirmation_code}
        """

        if self._send(email_subject='Confirmation Code', email_content=content):
            return self.confirmation_code

        return False

    def _send(self, email_subject, email_content, email_to=None):
        try:
            mail = EmailMessage()
            mail['Subject'] = email_subject
            mail['From'] = BASE_CONFIG.EMAIL_FROM_ADDRESS
            mail['To'] = email_to or self.email_address
            mail.set_content(email_content, subtype='html')

            # block outbound email if test/dev
            if app.config.get('TESTING') or app.config.get('BLOCK_OUTBOUND_EMAIL'):
                print('TESTING config enabled.. skipping smtp send')
                print('keygen', self.confirmation_code) if self.confirmation_code else None
                return True

            # otherwise, fire away
            with smtplib.SMTP_SSL('smtp.example.com', 465) as server:
                server.login(BASE_CONFIG.EMAIL_FROM_ADDRESS, BASE_CONFIG.EMAIL_FROM_PW)
                server.send_message(mail)
                server.quit()

            return True

        except Exception as error:
            print('Mail Failed', error)
            return False
