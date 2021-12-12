from mongoengine import connect, Document, IntField, StringField, DateTimeField
from internals.constants import database_name, host, database_port, wet, dry


def connect_database():
    connect(db=database_name, host=host, port=int(database_port))


class Plants(Document):
    plant_index = IntField(required=True)
    name = StringField(required=True)
    location_id = IntField()
    minimum_moisture = IntField(default=50)
    maximum_moisture = IntField(default=100)


class Locations(Document):
    location_id = IntField(required=True)
    location = StringField(required=True)


class Devices(Document):
    device_number = IntField(required=True)
    device_name = StringField(default='Arduino Uno')


class Moisture(Document):
    moisture_index = IntField(required=True)
    moisture_value = IntField(required=True)
    date_time = DateTimeField()


class Sensors(Document):
    sensor_index = IntField(required=True)
    device_number = IntField(default=1)
    wet_value = IntField(default=wet)
    dry_value = IntField(default=dry)


class Settings(Document):
    from_email = StringField()
    to_email = StringField()
    interval = IntField(default=60)


def write_plants(plant_index, name, location_id, minimum_moisture=None, maximum_moisture=None):
    post = Plants(plant_index=plant_index,
                  name=name,
                  location_id=location_id,
                  minimum_moisture=minimum_moisture,
                  maximum_moisture=maximum_moisture)
    post.save()


def write_location(location_id, location):
    post = Locations(location_id=location_id,
                     location=location)
    post.save()


def write_device(device_number, device_name=None):
    post = Devices(device_number=device_number,
                   device_name=device_name)
    post.save()


def write_moisture(moisture_index, moisture_value, date_time):
    post = Moisture(moisture_index=moisture_index,
                    moisture_value=moisture_value,
                    date_time=date_time)
    post.save()


def write_sensors(sensor_index, device_number=None, wet_value=None, dry_value=None):
    post = Sensors(sensor_index=sensor_index,
                   device_number=device_number,
                   wet_value=wet_value,
                   dry_value=dry_value)
    post.save()


def write_settings(from_email, to_email, interval=None):
    post = Settings(from_email=from_email,
                    to_email=to_email,
                    interval=interval)
    post.save()


def get_location_by_id(location_id):
    for entry in Locations.objects:
        if entry['location_id'] == location_id:
            return entry['location']


def get_locations():
    locations = []
    for entry in Locations.objects:
        locations.append({'location_id': entry['location_id'],
                          'location': entry['location']
                          })
    return locations


def get_devices():
    devices = []
    for entry in Devices.objects:
        devices.append({'device_number': entry['device_number'],
                        'device_name': entry['device_name']
                        })
    return devices


def get_plants_info():
    plants = []
    for entry in Plants.objects:
        plants.append({'plant_index': entry['plant_index'],
                       'name': entry['name'],
                       'location': get_location_by_id(entry['location_id'])
                       })
    return plants


def get_plant_by_index(plant_index):
    plants = get_plants_info()
    for plant in plants:
        if plant['plant_index'] == plant_index:
            return plant


def update_plant_by_index(plant_index, name, location_id, minimum_moisture, maximum_moisture):
    post = Plants.objects()[plant_index]
    Plants.objects(id=post.id).update_one(name=name,
                                          location_id=location_id,
                                          minimum_moisture=minimum_moisture,
                                          maximum_moisture=maximum_moisture
                                          )
    post.reload()


def delete_plant_by_index(plant_index):
    Plants.objects(plant_index=plant_index).delete()


def get_sensors():
    sensors = []
    for entry in Sensors.objects:
        sensors.append({'sensor_index': entry['sensor_index'],
                        'device_number': entry['device_number'],
                        'wet_value': entry['wet_value'],
                        'dry_value': entry['dry_value']
                        })
    return sensors


def get_available_sensors():
    available_sensors = [0, 1, 2, 3, 4, 5]
    for entry in Sensors.objects:
        if entry['sensor_index'] in available_sensors:
            available_sensors.remove(entry['sensor_index'])
    return available_sensors
