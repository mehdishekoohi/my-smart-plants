from flask import Flask, render_template, url_for, request
from internals.sensors import get_sensor_value, get_sensors_data
from internals.utils import get_current_status, get_plants_complete_stats
from internals.constants import my_plants


app = Flask(__name__)


@app.route("/")
def home():
    return "Welcome to homepage"


@app.route("/plants")
def plants():
    values = {'0': 110, '1': 10, '2': 4, '3': 55, '4': 80}
    plants_stats = get_plants_complete_stats(values=values, plants_list=my_plants)
    return render_template('template.html', plants=plants_stats)


@app.route("/plant")
def plant():
    sensor_index = request.args.get('index', default=0, type=int)
    values = {'0': 90, '1': 38, '2': 22, '3': 22, '4': 22}
    # values = get_sensors_data()
    current_value, image_filename = get_current_status(values=values, sensor_index=sensor_index)
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


if __name__ == '__main__':
    app.run(debug=True)
