# Simple demo of the LSM9DS1 accelerometer, magnetometer, gyroscope.
# Will print the acceleration, magnetometer, and gyroscope values every second.

import time
import datetime

import model # For saving the sensor data to the database

import board
import busio
import adafruit_lsm9ds1

# Create an instance of our data model access layer object.
# This object takes care of all the Peewee ORM and DB access so our code in this
# file is very simple and just calls function on the model access layer object.
data = model.SensorData()

# Define which sensors we expect to be connected to the Pi.
sensor1Name = 'LSM9DS1 X-Accelerometer'
sensor1Units = 'm/s^2'
sensor2Name = 'LSM9DS1 Y-Accelerometer'
sensor2Units = 'm/s^2'
sensor3Name = 'LSM9DS1 Z-Accelerometer'
sensor3Units = 'm/s^2'
sensor4Name = 'LSM9DS1 X-Magnetometer'
sensor4Units = 'Gauss'
sensor5Name = 'LSM9DS1 Y-Magnetometer'
sensor5Units = 'Gauss'
sensor6Name = 'LSM9DS1 Z-Magnetometer'
sensor6Units = 'Gauss'
sensor7Name = 'LSM9DS1 X-Gyroscope'
sensor7Units = 'degrees/sec'
sensor8Name = 'LSM9DS1 Y-Gyroscope'
sensor8Units = 'degrees/sec'
sensor9Name = 'LSM9DS1 Z-Gyroscope'
sensor9Units = 'degrees/sec'
sensor10Name = 'LSM9DS1 Temperature'
sensor10Units = '*Might not be °C'
sensor11Name = 'LSM9DS1 X-Accelerometer Average'
sensor11Units = 'Average m/s^2'
sensor12Name = 'LSM9DS1 Y-Accelerometer Average'
sensor12Units = 'Average m/s^2'
sensor13Name = 'LSM9DS1 Z-Accelerometer Average'
sensor13Units = 'Average m/s^2'
data.define_sensor(sensor1Name, sensor1Units)
data.define_sensor(sensor2Name, sensor2Units)
data.define_sensor(sensor3Name, sensor3Units)
data.define_sensor(sensor4Name, sensor4Units)
data.define_sensor(sensor5Name, sensor5Units)
data.define_sensor(sensor6Name, sensor6Units)
data.define_sensor(sensor7Name, sensor7Units)
data.define_sensor(sensor8Name, sensor8Units)
data.define_sensor(sensor9Name, sensor9Units)
data.define_sensor(sensor10Name, sensor10Units)
data.define_sensor(sensor11Name, sensor11Units)
data.define_sensor(sensor12Name, sensor12Units)
data.define_sensor(sensor13Name, sensor13Units)

# I2C connection:
i2c = busio.I2C(board.SCL, board.SDA)
sensor = adafruit_lsm9ds1.LSM9DS1_I2C(i2c)

# SPI connection:
# from digitalio import DigitalInOut, Direction
# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# csag = DigitalInOut(board.D5)
# csag.direction = Direction.OUTPUT
# csag.value = True
# csm = DigitalInOut(board.D6)
# csm.direction = Direction.OUTPUT
# csm.value = True
# sensor = adafruit_lsm9ds1.LSM9DS1_SPI(spi, csag, csm)

# Main loop will read the acceleration, magnetometer, gyroscope, Temperature
# values every second and print them out.

try:
    while True:

        timeout = time.time() + 1#60*2   # 2 minutes from now
        loops = 0   # loop counter

        # Initalizes the max values of the min and max values and the begining sum values
        accel_x_min = 100
        accel_y_min = 100
        accel_z_min = 100
        accel_x_max = -100
        accel_y_max = -100
        accel_z_max = -100
        accel_x_sum = 0
        accel_y_sum = 0
        accel_z_sum = 0

        while True:
            # Break loop after two minutes
            if time.time() >= timeout:
                break

            # increment loops by 1
            loops += 1

            # Read acceleration, magnetometer, gyroscope, temperature.
            accel_x, accel_y, accel_z = sensor.acceleration
            mag_x, mag_y, mag_z = sensor.magnetic
            gyro_x, gyro_y, gyro_z = sensor.gyro
            temp = sensor.temperature

            # Rounds sensor data before it is put in the database and printed
            accel_x = round(accel_x, 3)
            accel_y = round(accel_y, 3)
            accel_z = round(accel_z, 3)
            mag_x = round(mag_x, 3)
            mag_y = round(mag_y, 3)
            mag_z = round(mag_z, 3)
            gyro_x = round(gyro_x, 3)
            gyro_y = round(gyro_y, 3)
            gyro_z = round(gyro_z, 3)
            temp = round(temp, 3)

            # keep track of max, min, and average values for acceleration
            # if accel_x > accel_x_max:
            #     accel_x_max = accel_x
            # if accel_y > accel_y_max:
            #     accel_y_max = accel_y
            # if accel_z > accel_z_max:
            #     accel_z_max = accel_z
            # if accel_x < accel_x_min:
            #     accel_x_min = accel_x
            # if accel_y < accel_y_min:
            #     accel_y_min = accel_y
            # if accel_z < accel_z_min:
            #     accel_z_min = accel_z
            accel_x_sum += accel_x
            accel_y_sum += accel_y
            accel_z_sum += accel_z

        accel_x_avg = accel_x_sum / loops
        accel_y_avg = accel_y_sum / loops
        accel_z_avg = accel_z_sum / loops

        # Get the current time for this batch of sensor readings.
        reading_time = datetime.datetime.now()

        # Print values.
        print("Reading Sensor -> LSM9DS1: Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f}), Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f}), Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f}), Temperature: {0:0.3f}°C (Might not be in °C)".format(accel_x, accel_y, accel_z, mag_x, mag_y, mag_z, gyro_x, gyro_y, gyro_z, temp))

        # Add the sensor readings to the database.
        data.add_reading(time=reading_time, name='{0}'.format(sensor1Name), value=accel_x)
        data.add_reading(time=reading_time, name='{0}'.format(sensor2Name), value=accel_y)
        data.add_reading(time=reading_time, name='{0}'.format(sensor3Name), value=accel_z)
        data.add_reading(time=reading_time, name='{0}'.format(sensor4Name), value=mag_x)
        data.add_reading(time=reading_time, name='{0}'.format(sensor5Name), value=mag_y)
        data.add_reading(time=reading_time, name='{0}'.format(sensor6Name), value=mag_z)
        data.add_reading(time=reading_time, name='{0}'.format(sensor7Name), value=gyro_x)
        data.add_reading(time=reading_time, name='{0}'.format(sensor8Name), value=gyro_y)
        data.add_reading(time=reading_time, name='{0}'.format(sensor9Name), value=gyro_z)
        data.add_reading(time=reading_time, name='{0}'.format(sensor10Name), value=temp)
        data.add_reading(time=reading_time, name='{0}'.format(sensor11Name), value=accel_x_avg)
        data.add_reading(time=reading_time, name='{0}'.format(sensor12Name), value=accel_y_avg)
        data.add_reading(time=reading_time, name='{0}'.format(sensor13Name), value=accel_z_avg)

        # # Wait 30 seconds and repeat.
        # time.sleep(120.0)
finally:
    # Finally close the connection to the database when done.
    data.close()

def readXYAccel():
    # Read acceleration, magnetometer, gyroscope, temperature.
    accel_x, accel_y, accel_z = sensor.acceleration
    mag_x, mag_y, mag_z = sensor.magnetic
    gyro_x, gyro_y, gyro_z = sensor.gyro
    temp = sensor.temperature
    # Print values.
    print("Acceleration (m/s^2): ({0:0.3f},{1:0.3f},{2:0.3f})".format(accel_x, accel_y, accel_z))
    print("Magnetometer (gauss): ({0:0.3f},{1:0.3f},{2:0.3f})".format(mag_x, mag_y, mag_z))
    print("Gyroscope (degrees/sec): ({0:0.3f},{1:0.3f},{2:0.3f})\n".format(gyro_x, gyro_y, gyro_z))

    return accel_x, accel_y
