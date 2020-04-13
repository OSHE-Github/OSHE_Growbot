import time
import datetime

import model # For saving the sensor data to the database

from board import SCL, SDA
import busio

from adafruit_seesaw.seesaw import Seesaw

# Create an instance of our data model access layer object.
# This object takes care of all the Peewee ORM and DB access so our code in this
# file is very simple and just calls function on the model access layer object.
data = model.SensorData()

# Define which sensors we expect to be connected to the Pi.
sensor1Name = 'SeeSaw Soil Temperature'
sensor1Units = '°C'
sensor2Name = 'SeeSaw Soil Moisture'
sensor2Units = '%'
data.define_sensor(sensor1Name, sensor1Units)
data.define_sensor(sensor2Name, sensor2Units)

i2c_bus = busio.I2C(SCL, SDA)

ss = Seesaw(i2c_bus, addr=0x36)

try:
    while True:
        # Get the current time for this batch of sensor readings.
        reading_time = datetime.datetime.now()

        # read moisture level through capacitive touch pad 200 - 2000
        touch = ss.moisture_read()
        touch = ((touch - 200)/1800)*100
        touch = round(touch, 2)

        # read temperature from the temperature sensor
        temp = ss.get_temp()
        temp = round(temp, 2)

        # Print out sensor values
        print("Reading Sensor -> SeeSaw Soil: Temperature: " + str(temp) + "°C,  Moisture: " + str(touch) + "%")

        # Add the sensor readings to the database.
        data.add_reading(time=reading_time, name='{0}'.format(sensor1Name), value=temp)
        data.add_reading(time=reading_time, name='{0}'.format(sensor2Name), value=touch)

        # Wait 30 seconds and repeat.
        time.sleep(120.0)
finally:
    # Finally close the connection to the database when done.
    data.close()
