from apscheduler.schedulers.blocking import BlockingScheduler
from internals.sensors import get_data
from datetime import datetime

date_format = '%A %B %d, %Y %H:%M:%S'
moisture_alarm = 500


def get_values(date_format):
    formatted_date = datetime.now().strftime(date_format)
    print(f'{formatted_date} >>> {get_data()}')

    plants_list = [{'name': 'a0', 'value': get_data()[0]},
                   {'name': 'a1', 'value': get_data()[1]}]

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
