from apscheduler.schedulers.blocking import BlockingScheduler
from internals.sensors import get_sensors_data
from internals.constants import plants_csv, moisture_alarm, template_email, output_email, \
    from_email, to_email, interval_minutes
from internals.utils import get_dry_plants, insert_text_into_mail_body, generate_random_values, \
    get_plants_name_from_csv, get_values_percentage
from internals.mailing import send_email
from datetime import datetime
import os

my_plants = get_plants_name_from_csv(plants_csv)


def plants_report():
    sensor_data = get_sensors_data()
    values = get_values_percentage(sensor_data)
    # values = generate_random_values(sensors_number=5)
    date_format = '%Y-%M-%d, %H:%M'
    date = datetime.now().strftime(date_format)
    print(f'{date}: Checking moisture values')
    dry_plants = get_dry_plants(my_plants, values, moisture_alarm)
    if len(dry_plants):
        print(f'Found dry plants:')
        for p in dry_plants:
            print(p)
        insert_text_into_mail_body(mail_template=template_email, output_file=output_email,
                                   plants_complete_list=dry_plants)
        response_code = send_email(email_file=output_email, from_email=from_email, to_email=to_email)
        if response_code == 202:
            os.remove(output_email)
    else:
        print('No dry plants, all is good!')
    print('--------------------------')


# run for the fist time
plants_report()

# set scheduler and repeat it
scheduler = BlockingScheduler()
scheduler.add_job(plants_report, 'interval', minutes=interval_minutes)
scheduler.start()
