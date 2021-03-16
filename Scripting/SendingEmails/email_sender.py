import smtplib
from email.message import EmailMessage
from string import Template
from pathlib import Path

html = Template(Path('index.html').read_text())
email = EmailMessage()
email['from'] = 'PyCharm Development Team'
email['to'] = 'basavarajuanudeep@gmail.com'
email['subject'] = 'Hello Greeting!'

email.set_content(html.substitute(name = 'Anudeep'),'html')

with smtplib.SMTP(host='smtp.gmail.com',port=587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.login('basavarajuanudeep@gmail.com','July.me@97')
    smtp.send_message(email)
    print('All good Boss!')