from mailer import Mailer

mailer = Mailer("emails.csv", toCaptcha="contra")
mailer.process_file()
mailer.close()

