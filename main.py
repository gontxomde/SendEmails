from mailer import Mailer
import logging
logging.basicConfig(filename='app.log',level = logging.INFO, filemode='w', format='%(asctime)s - %(levelname)s - %(message)s')

mailer = Mailer("emails.csv", toCaptcha="contra")
mailer.process_file()
mailer.close()

