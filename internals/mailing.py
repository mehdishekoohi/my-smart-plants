from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os

api_key = os.getenv('SENDGRID_API_KEY')
# api_key ='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'


if not api_key:
    print('"api_key" is not exported. Use export SENDGRID_API_KEY="<YOUR-SENDGRID-API-KEY>"')
    exit(1)


def send_email(email_file, from_email, to_email):
    print('Sending mail ...')
    with open(os.path.join(os.getcwd(), email_file), 'r') as file:
        html_content = file.read()
        file.close()
    message = Mail(
        from_email=from_email,
        to_emails=to_email,
        subject='My Smart Plants Report',
        html_content=html_content)
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print('Email sent!')
        return response.status_code
    except Exception as e:
        print(e.message)
