from email.message import EmailMessage
from app import password
import ssl
import smtplib

email_sender = "me@gmaiil.com" #The person mail who is sending a message
email_password = password #Here comes the password imported from app file

email_receiver = "you@gmail.com" #The person who will receive the message

subject = "Greetings"
body = """
Hello, sister! How have you been? How's mom and dad? I am coming home on this weekend. Can't wait to see ya all!\nWarm Regards, Aliyan!
"""

em = EmailMessage() #Creating an instance of EmailMessage class
em["from"] = email_sender
em["to"] = email_receiver
em["subject"] = subject
em.set_content(body)

context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as smtp:
    smtp.login(email_sender, email_password)
    smtp.sendmail(email_sender, email_receiver, em.as_string())