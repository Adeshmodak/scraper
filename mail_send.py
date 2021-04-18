import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders

def send(filename):
    from_add = 'adesh2939modak@gmail.com'
    to_add = 'testadesh@zohomail.in'
    subject = "stock market details"
    msg = MIMEMultipart()
    msg['From'] = from_add
    msg['To'] = to_add
    msg['subject'] = subject

    body="<b> todays finance report </b>"

    msg.attach(MIMEText(body,'html'))
    my_file=open(filename,'rb')

    part=MIMEBase('application','octate-stream')
    part.set_payload(my_file.read())
    encoders.encode_base64(part)
    part.add_header('content-disposition','attachment; filename='+filename)
    msg.attach(part)
    message = msg.as_string()
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.starttls()
    server.login(from_add, 'sdvuvlruwkkpskjl')
    server.sendmail(from_add, to_add, message)
    server.quit()
