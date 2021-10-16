from internals.sensors import get_sensors_data, get_sensor_value
from internals.constants import levels, plant_line_number, date_line_number
from datetime import datetime
import random


def generate_random_values():
    values = {}
    for i in range(0, 6):
        values[str(i)] = random.randint(0, 100)
    return values


def get_percentage(value, wet, dry):
    return int(round((value - wet) * ((dry - wet) / 1000), 0))


def get_current_status(values, sensor_index):
    current_value = get_sensor_value(values, sensor_index=sensor_index)
    if current_value >= levels['high']:
        image_filename = 'green.png'
    elif levels['mid'] + 1 < current_value < levels['high']:
        image_filename = 'yellow.png'
    elif levels['low'] + 1 < current_value <= levels['mid']:
        image_filename = 'red.png'
    elif levels['danger'] < current_value <= levels['low']:
        image_filename = 'wow.png'
    else:
        image_filename = 'dead.png'
    return current_value, image_filename


def get_plants_complete_stats(values, plants_list):
    for index in values.keys():
        for p in plants_list:
            if p['index'] == index:
                current_value, image_filename = get_current_status(values=values, sensor_index=index)
                p['value'] = current_value
                p['image'] = image_filename
    return plants_list


def plant_h3_text(plant_name, location, percentage):
    return f'<h3 style="text-align: inherit; font-family: inherit">' \
           f'<span style="color: #f4f4f4">{plant_name} ({location}): {percentage}%</span></h3>\n'


def date_text(date):
    return f'<div style="font-family: inherit; text-align: center">{str(date)}</div>'


def insert_text_into_mail_body(mail_template, output_file, plants_complete_list: list):
    date_format = '%A %B %d %Y, %H:%M'
    date = datetime.now().strftime(date_format)
    dtext = date_text(date)
    complete_text = ''
    for p in plants_complete_list:
        complete_text += (plant_h3_text(plant_name=p['name'], location=p['location'], percentage=p['value']))
    with open(mail_template, "r") as f:
        contents = f.readlines()
    contents.insert(date_line_number, dtext)
    contents.insert(plant_line_number, complete_text)
    with open(output_file, "w") as f:
        contents = "".join(contents)
        f.write(contents)


def get_dry_plants(plants_list, values, moisture_alarm):
    plants = get_plants_complete_stats(values, plants_list)
    dry_plants = []
    for key, value in values.items():
        if value < moisture_alarm:
            for p in plants:
                if p['index'] == key:
                    dry_plants.append(p)
    return dry_plants
