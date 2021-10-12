from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail
import os


def send_email(api_key, dry_plants):
    with open(os.path.join(os.getcwd(), 'templates', 'email.html'), 'r') as file:
        html_content = file.read()
        file.close()

    message = Mail(
        from_email='smartplants@shokoohi.ca',
        to_emails='mehdishekoohi@gmail.com',
        subject='My Smart Plants: ',
        html_content=html_content.replace('PlantNameHere', 'Rose'))
    try:
        sg = SendGridAPIClient(api_key)
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)

    print('All done!')
