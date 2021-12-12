from flask import Flask, render_template, request, url_for, jsonify
from internals.sensors import get_sensors_data
from internals.utils import get_plants_complete_stats, get_plants_name_from_csv, get_values_percentage, \
    get_ip, generate_random_values
from internals.constants import plants_csv, wet, dry
from internals.database import write_plants, connect_database, get_location_by_id, \
    get_sensors, write_sensors, get_available_sensors, get_devices


my_plants = get_plants_name_from_csv(plants_csv)
host_ip = get_ip()

app = Flask(__name__)


# todo: to be complete later
@app.route("/")
def home():
    return render_template('home.html')


@app.route("/plants")
def plants():
    # comment for testing
    sensor_data = get_sensors_data()
    values = get_values_percentage(sensor_data)
    # uncomment for testing
    # values = generate_random_values(sensors_number=5)
    plants_stats = get_plants_complete_stats(values=values, plants_list=my_plants)
    return render_template('template.html', plants=plants_stats)


# todo: complete this rout
@app.route("/plant")
def plant():
    sensor_index = request.args.get('index', default=0, type=int)
    pass


@app.route("/sensors", methods=['GET', 'POST'])
def sensors():
    connect_database()
    if request.method == 'GET':
        available_sensors = get_available_sensors()
        sensors_list = get_sensors()
        if len(sensors_list) == 0:
            sensors_list = [{'sensor_index': '-', 'device_number': '-', 'wet_value': '-', 'dry_value': '-'}]
        return render_template("sensors.html", sensors=sensors_list,
                               default_wet=wet, default_dry=dry,
                               available_sensors=available_sensors,
                               )
    if request.method == 'POST':
        available_sensors = get_available_sensors()
        response = request.form
        sensor_index = response['sensor_index']
        wet_value = response['wet_value']
        dry_value = response['dry_value']
        write_sensors(sensor_index, wet_value, dry_value)
        sensors_list = get_sensors()
        return render_template("sensors.html", sensors=sensors_list, available_sensors=available_sensors)


@app.route("/sensor", methods=['GET'])
def sensor():
    return render_template("add_sensor.html")


@app.route("/add_sensor", methods=['POST', 'GET'])
def add_sensor():
    if request.method == 'POST':
        response = request.form
        sensor_index = response['sensor_index']
        device_number = response['device_number']
        wet_value = response['wet_value']
        dry_value = response['dry_value']
        return f'{sensor_index} {device_number} {wet_value} {dry_value}'
    else:
        return render_template('add_sensor.html')


@app.route("/setting", methods=['GET'])
def setting():
    return render_template("setting.html")


@app.route('/results', methods=['POST', 'GET'])
def results():
    if request.method == 'POST':
        response = request.form
        connect_database()
        plant_name = response['plant_name']
        sensor_index = response['sensor_index']
        location_id = response['location_id']
        location_name = get_location_by_id(int(location_id[0]))
        minimum_moisture = response['minimum_moisture']
        maximum_moisture = response['maximum_moisture']
        write_plants(sensor_index[0], plant_name[0], location_id[0], minimum_moisture[0], maximum_moisture[0])
        return f"Plant {plant_name[0]} (sensor index: {sensor_index[0]}) added to {location_name}"


if __name__ == '__main__':
    app.run(debug=True)
