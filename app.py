from flask import Flask, render_template, url_for
from internals.sensors import get_data

app = Flask(__name__)


@app.route("/")
def index():
    current_value = get_data()
    if current_value > 60:
        image_filename = 'green.png'
    elif 30 < current_value < 59:
        image_filename = 'yellow.png'
    else:
        image_filename = 'red.png'
    return render_template('template.html', current_value=current_value, image_filename=image_filename)


if __name__ == '__main__':
    app.run(debug=True)
