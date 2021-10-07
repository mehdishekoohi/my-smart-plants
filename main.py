from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from internals.sensors import get_sensors_data
from internals.constants import plants_list


from time import sleep


date_format = '%A %B %d, %Y %H:%M:%S'
moisture_alarm = 50


def get_values(date_format):
    values = get_sensors_data()
    formatted_date = datetime.now().strftime(date_format)
    print(f'{formatted_date} >>> {values}')

    dry_plants = []
    for i, plant in enumerate(plants_list):
        if plant['value'] > moisture_alarm:
            dry_plants.append(plants_list[i])
            print(f'Need water for {plant["name"]}')


get_values(date_format=date_format)


def repeater():
    get_values(date_format=date_format)


scheduler = BlockingScheduler()
scheduler.add_job(repeater, 'interval', seconds=5)
scheduler.start()
