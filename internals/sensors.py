import serial
import json
from time import sleep


def get_sensors_data() -> dict:
    data = None
    sleep(1)
    for i in range(1, 11):
        while True:
            sleep(1)
            ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=2)
            try:
                data = ser.readline().decode('utf-8').replace('\r\n', '').replace("'", '"')
            except ValueError:
                print('Could not get data, make sure Arduino device and sensor is connected')
                pass
            except serial.serialutil.SerialException:
                print('Device not found, check the connection')
                pass
            except FileNotFoundError:
                print('Device not found, check the connection')
                pass
            try:
                values = json.loads(str(data))
                return values
            except json.decoder.JSONDecodeError:
                continue
        break


def get_sensor_value(sensors_data, sensor_index):
    try:
        return sensors_data[str(sensor_index)]
    except KeyError:
        print('Send valid sensor index')
