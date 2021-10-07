from internals.sensors import get_sensors_data, get_sensor_value


def get_percentage(value, wet, dry):
    return int(round((value - wet) * ((dry - wet)/1000), 0))


def get_current_status(values, sensor_index):
    # values = get_sensors_data()
    current_value = get_sensor_value(values, sensor_index=sensor_index)
    if current_value >= 60:
        image_filename = 'green.png'
    elif 41 < current_value < 60:
        image_filename = 'yellow.png'
    elif 21 <= current_value <= 40:
        image_filename = 'red.png'
    elif 5 <= current_value <= 20:
        image_filename = 'wow.png'
    else:
        image_filename = 'dead.png'
    return current_value, image_filename
