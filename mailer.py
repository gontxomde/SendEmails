from configparser import ConfigParser
import smtplib
from os.path import basename
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.utils import COMMASPACE, formatdate
import pandas as pd
from captcha.image import ImageCaptcha

class Mailer():
    """
    Class to send multiple emails based on the data of a csv
    """
    def __init__(self, filePath = "emails.csv", toCaptcha = []):

        self.configure_service()
        print("Servicio configurado")
        self.smtp = smtplib.SMTP(self.server,self.port) 
        self.smtp.ehlo()
        self.smtp.starttls()
        self.smtp.login(self.user, self.password)
        self.filePath = filePath
        if isinstance(toCaptcha, str):
            self.toCaptcha = [toCaptcha]
        elif isinstance(toCaptcha, list):
            self.toCaptcha = toCaptcha
        else:
            raise TypeError("toCaptcha should be a string or a list of strings")

    

    def configure_service(self):
        config = ConfigParser()
        config.read('config_secret.ini')
        self.user = config.get('Office-365-Credentials', 'email')
        self.password = config.get('Office-365-Credentials', 'password')
        self.server = config.get('Office-365-Credentials', 'server')
        self.port = config.get('Office-365-Credentials', 'port')
        config.read('config.ini')
        self.body = config.get('body', 'text')
        self.subject = config.get('body', 'subject')

    def close(self):
        self.smtp.close()

    def process_file(self):
        self.data = pd.read_csv(self.filePath, header = 0)
        assertionMessage = "The columns should equal the number of  \{ \} in the message + 1"
        if len(self.toCaptcha) > 0:
            assertionMessage =  "+ number of captchable columns."
        else:
            assertionMessage += "."
        assert self.body.count('{') == self.data.shape[1]-len(self.toCaptcha)-1, assertionMessage

        columns = self.data.cols[1:]

        for _, row in self.data.iterrows():
            files = []
            textParts = []
            for element in self.data.columns[1:]:
                if element in self.toCaptcha:
                    try:
                        filename = '{}.png'.format(element)
                        image = ImageCaptcha(width =  len(row[element]*30))
                        image.write(row[element], filename)
                        files.append(filename)
                    except:
                        print("The column {} you wanna captcha is not a column of the .csv".format(element))
                else:
                    textParts.append(row[element])

            self.send_mail(
                send_to = row[0],
                text = self.body.format(*textParts),
                files = files

            )
            print(f"Enviado a {row[0]}")


    def send_mail(self, send_to, text,files=None ):
        print(send_to)
        send_to = [send_to]
        print(send_to)
        msg = MIMEMultipart()
        msg['From'] = self.user
        msg['To'] = COMMASPACE.join(send_to)
        msg['Date'] = formatdate(localtime=True)
        msg['Subject'] = self.subject

        msg.attach(MIMEText(text))

        for f in files or []:
            with open(f, "rb") as fil:
                part = MIMEApplication(
                    fil.read(),
                    Name=basename(f)
                )
            # After the file is closed
            part['Content-Disposition'] = 'attachment; filename="%s"' % basename(f)
            msg.attach(part)
        
        self.smtp.sendmail(self.user, send_to, msg.as_string())