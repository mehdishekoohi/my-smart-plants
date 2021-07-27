import serial


def get_data():
    ser = serial.Serial('/dev/ttyACM0', baudrate=9600, timeout=2)
    try:
        data = ser.readline().decode('utf-8').replace('\r\n', '')
    except ValueError:
        print('Could not get data, make sure Arduino device and sensor is connected')
        data = 0
        pass
    except serial.serialutil.SerialException:
        print('Device not found, check the connection')
        data = 0
        pass
    except FileNotFoundError:
        print('Device not found, check the connection')
        data = 0
        pass
    if data:
        return int(data)

