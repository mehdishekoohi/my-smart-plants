from internals.sensors import get_sensor_value
from internals.constants import levels, plant_line_number, date_line_number, wet, dry
from datetime import datetime
import random
import csv
import socket


def get_plants_name_from_csv(csv_file):
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        plants = []
        for row in reader:
            plants.append({'index': row[0], 'name': row[1], 'location': row[2]})
    file.close()
    plants.pop(0)
    return plants


def add_new_plant(csv_file, name, location):
    with open(csv_file, 'a+', newline='\n') as file:
        plants_number = len(get_plants_name_from_csv(csv_file)) - 1
        csv_writer = csv.writer(file)
        csv_writer.writerow([plants_number + 1, name, location])
        file.close()


def generate_random_values(sensors_number: int):
    values = {}
    for i in range(0, sensors_number + 1):
        values[str(i)] = random.randint(0, 100)
    return values


def get_percentage(value):
    dryness = int(round((value - wet) * ((dry - wet) / 1000), 0))
    wet_percentage = 100 - dryness
    if wet_percentage >= 100:
        return 100
    elif wet_percentage <= 0:
        return 0
    else:
        return wet_percentage


def get_values_percentage(values: dict):
    percentages = {}
    for key, value in values.items():
        percentages[key] = get_percentage(value)
    return percentages


def get_current_status(values, sensor_index):
    current_value = get_sensor_value(values, sensor_index=sensor_index)
    if current_value >= levels['high']:
        image_filename = 'green.png'
    elif levels['mid'] + 1 <= current_value < levels['high']:
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


def get_ip():
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    s.connect(('10.255.255.255', 1))
    ip = s.getsockname()[0]
    s.close()
    return ip
