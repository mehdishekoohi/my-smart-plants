from apscheduler.schedulers.blocking import BlockingScheduler
from internals.sensors import get_sensors_data
from internals.constants import my_plants, moisture_alarm, template_email, output_email, from_email, to_email
from internals.utils import get_dry_plants, insert_text_into_mail_body, generate_random_values
from internals.mailing import send_email
from datetime import datetime
import os

# values = get_sensors_data()


def plants_report():
    values = generate_random_values()
    date_format = '%Y-%M-%d, %H:%M : '
    date = datetime.now().strftime(date_format)
    dry_plants = get_dry_plants(my_plants, values, moisture_alarm)
    if len(dry_plants):
        print(f'{date}Found dry plants, sending email ...')
        for p in dry_plants:
            print(p)
        insert_text_into_mail_body(mail_template=template_email, output_file=output_email,
                                   plants_complete_list=dry_plants)
        response_code = send_email(email_file=output_email, from_email=from_email, to_email=to_email)
        if response_code == 202:
            os.remove(output_email)
    print('----------------------')


scheduler = BlockingScheduler()
scheduler.add_job(plants_report, 'interval', seconds=10)
scheduler.start()
