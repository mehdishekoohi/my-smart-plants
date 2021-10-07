from flask import Flask, render_template, url_for
from internals.sensors import get_sensor_value, get_sensors_data
from internals.utils import get_current_status
from internals.constants import wet, dry


app = Flask(__name__)


@app.route("/sensors")
def sensors():
    values = {'0': 110, '1': 38, '2': 22, '3': 22, '4': 22}
    current_value, image_filename = get_current_status(values=values, sensor_index=0)
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


@app.route("/sensor0")
def sensor0():
    values = get_sensors_data()
    current_value, image_filename = get_current_status(values=values, sensor_index=0)
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


@app.route("/sensor1")
def sensor1():
    values = get_sensors_data()
    current_value, image_filename = get_current_status(values=values, sensor_index=1)
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


@app.route("/sensor2")
def sensor2():
    values = get_sensors_data()
    current_value, image_filename = get_current_status(values=values, sensor_index=2)
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


@app.route("/sensor3")
def sensor3():
    values = get_sensors_data()
    current_value, image_filename = get_current_status(values=values, sensor_index=3)
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


@app.route("/sensor4")
def sensor4():
    values = get_sensors_data()
    current_value, image_filename = get_current_status(values=values, sensor_index=4)
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


if __name__ == '__main__':
    app.run(debug=True)
