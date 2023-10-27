from email.message import EmailMessage
import ssl
import smtplib

email_sender = 'jwlarbi15@gmail.com'
email_password = ''

email_receiver=''

subject='I love you'

body = """
You're gonna be great!!!
"""

em = EmailMessage()
em['From'] = email_sender
em['To'] = email_receiver
em['subject'] = subject
em.set_content(body)

context = ssl.create_default_context()
with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context)