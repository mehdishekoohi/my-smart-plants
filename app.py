from flask import Flask, render_template, request
from internals.sensors import get_sensors_data
from internals.utils import get_plants_complete_stats, get_plants_name_from_csv, get_values_percentage, get_ip
from internals.constants import plants_csv

my_plants = get_plants_name_from_csv(plants_csv)
host_ip = get_ip()

print(f'Running app on "http://{host_ip}":5000')

app = Flask(__name__)


@app.route("/homepage")
def home():
    return "Welcome to homepage"


@app.route("/")
def plants():
    sensor_data = get_sensors_data()
    values = get_values_percentage(sensor_data)
    # values = generate_random_values(sensors_number=5)
    plants_stats = get_plants_complete_stats(values=values, plants_list=my_plants)
    return render_template('template.html', plants=plants_stats)


# todo: complete this rout
@app.route("/plant")
def plant():
    sensor_index = request.args.get('index', default=0, type=int)
    # todo
    pass


if __name__ == '__main__':
    app.run(host=get_ip(), port=5000, debug=True)
