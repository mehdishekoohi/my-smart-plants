from configparser import ConfigParser

config = ConfigParser()
config.read('config.ini')

# read email settings from config file
from_email = config['mail']['from_email']
to_email = config['mail']['to_email']

# read config settings from config file
wet = int(config['sensor']['wet'])
dry = int(config['sensor']['dry'])
moisture_alarm = int(config['sensor']['moisture_alarm'])
interval_minutes = int(config['interval']['minutes'])

# email template
template_email = 'templates/email.html'
output_email = 'email_output.html'

# line numbers to insert date and plants report
date_line_number = 153
plant_line_number = 176

# levels to indicate plants status
levels = {'high': 60, 'mid': 40, 'low': 20, 'danger': 10}
plants_csv = 'plants.csv'
