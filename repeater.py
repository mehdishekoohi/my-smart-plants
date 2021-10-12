from apscheduler.schedulers.blocking import BlockingScheduler
from datetime import datetime
from internals.sensors import get_sensors_data
from internals.constants import my_plants, moisture_alarm


date_format = '%A %B %d, %Y %H:%M:%S'


def get_values(date_format):
    # values = get_sensors_data()
    values = {'0': 110, '1': 10, '2': 4, '3': 49, '4': 80}
    formatted_date = datetime.now().strftime(date_format)
    print(f'{formatted_date} >>> {values}')

    dry_plants_index = []
    for key, value in values.items():
        if value < moisture_alarm:
            dry_plants_index.append(key)
    # for i, plant in enumerate(my_plants):
    #     if plant['index'] == str(i):
    #         if plant['value'] > moisture_alarm:
    #             dry_plants.append(my_plants[i])
    #             print(f'Need water for {plant["name"]}')
    return dry_plants_index


drys = get_values(date_format=date_format)


def repeater():
    get_values(date_format=date_format)


scheduler = BlockingScheduler()
scheduler.add_job(repeater, 'interval', seconds=5)
scheduler.start()
