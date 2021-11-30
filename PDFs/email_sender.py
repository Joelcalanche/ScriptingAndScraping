import smtplib

from email.message import EmailMessage
from string import Template

from pathlib import Path

html = Template(Path('index.html').read_text())


email = EmailMessage()

email['from'] = 'Joel calanche'

email['to'] = 'jacalanchec@estudiante.unexpo.edu.ve'

email['subject']= 'You won 1,000,000 dollars!'

# contenido de mensaje
# email.set_content('I am a Python Master')
# si quiero sustituir varias cosas puedo usar un diccionario

email.set_content(html.substitute({'name': 'TinTin'}), 'html')


with smtplib.SMTP(host='smtp.gmail.com', port=587) as smtp:
    smtp.ehlo()
    #encription
    smtp.starttls()
    smtp.login('joelcalanche96@gmail.com', 'calanche1996')
    smtp.send_message(email)
    print('all good boss!')
