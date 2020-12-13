import smtplib, ssl, sys

port = 465 
smtp_server = "smtp.gmail.com"
sender_email = "[sender]" 
password = "[sender password]"
receiver_email = sys.argv[1]
message = """\
Subject: Confirmatin code.

Your confirmation code is """ + sys.argv[2]

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)