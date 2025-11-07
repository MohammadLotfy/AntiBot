from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib

def send_email(subject, body, to):
    fromemali = "mohammad.latif.singin@gmail.com"
    password = "zzeoiblocdotoekw"
    msg = MIMEMultipart()
    msg['From'] = fromemali
    msg['To'] = to
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    try:
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(fromemali, password)
        server.send_message(msg)
        status = True
    except:
        status = False

    return status
