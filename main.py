from emails import send_mail
import pandas as pd
from configparser import ConfigParser
import smtplib




config = ConfigParser()
config.read('config_secret.ini')
user = config.get('Office-365-Credentials', 'email')
password = config.get('Office-365-Credentials', 'password')
server = config.get('Office-365-Credentials', 'server')
port = config.get('Office-365-Credentials', 'port')
config.read('config.ini')
body = config.get('body', 'text')
subject = config.get('body', 'subject')


smtp = smtplib.SMTP(server,port) 
smtp.ehlo()
smtp.starttls()
smtp.login(user, password)

data = pd.read_csv('emails.csv', header = None)

assert body.count('{') == data.shape[1]


for index, row in data.iterrows():

    send_mail(
        send_from = user,
        send_to = [row[0]],
        subject = subject,
        text = body.format(*row[1:]),
        smtp = smtp
    )
smtp.close()

