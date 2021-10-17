from flask import Flask, render_template, url_for, request
from internals.sensors import get_sensor_value, get_sensors_data
from internals.utils import get_current_status, get_plants_complete_stats
from internals.constants import my_plants
from internals.utils import generate_random_values


app = Flask(__name__)


@app.route("/homepage")
def home():
    return "Welcome to homepage"


@app.route("/")
def plants():
    values = generate_random_values(sensors_number=5)
    plants_stats = get_plants_complete_stats(values=values, plants_list=my_plants)
    return render_template('template.html', plants=plants_stats)


@app.route("/plant")
def plant():
    sensor_index = request.args.get('index', default=0, type=int)
    values = generate_random_values(sensors_number=5)
    # values = get_sensors_data()
    current_value, image_filename = get_current_status(values=values, sensor_index=sensor_index)
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


if __name__ == '__main__':
    app.run(debug=False)
