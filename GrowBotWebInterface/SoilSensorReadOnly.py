#Wilson Holmes
#Open Source Hardware Enterprise
#Growbot
#Created: 2020/04/??
#Last Modified: 2020/04/16
#Description: Adafruit_seesaw sensor. Will print and store the capacatance and temperature of the soil in the database on a timed interval.


import time
import datetime

# For saving the sensor data to the database
import model

# Imports required for this particular sensor
from board import SCL, SDA
import busio
from adafruit_seesaw.seesaw import Seesaw

# Create an instance of our data model access layer object.
# This object takes care of all the Peewee ORM and DB access so our code in this
# file is very simple and just calls function on the model access layer object.
data = model.SensorData()

# Define which sensors we expect to be connected to the Pi and their units.
sensor1Name = 'SeeSaw Soil Temperature'
sensor1Units = '°C'
sensor2Name = 'SeeSaw Soil Moisture'
sensor2Units = '%'

# If there are no prexisting entrys into the sensor table in the databse with these exact names and units, then a new entry will be created in the table.
data.define_sensor(sensor1Name, sensor1Units)
data.define_sensor(sensor2Name, sensor2Units)

# Does i2c stuff to be able to read the sensor data
i2c_bus = busio.I2C(SCL, SDA)
ss = Seesaw(i2c_bus, addr=0x36)

try:
    # Loop to continually add data to the database.
    while True:
        # Get the current time for this batch of sensor readings.
        reading_time = datetime.datetime.now()

        # Read sensor moisture level through capacitive touch pad (200 - 2000)
        touch = ss.moisture_read()
        # Use math to get values to be a percentage
        touch = ((touch - 200)/1800)*100
        touch = round(touch, 2) # Rounds data to 2 decimal places

        # Read sensor temperature
        temp = ss.get_temp()
        temp = round(temp, 2)   # Rounds data to 2 decimal places

        # Print out sensor values
        print("Reading Sensor -> SeeSaw Soil: Temperature: " + str(temp) + "°C,  Moisture: " + str(touch) + "%")

        # Add the sensor readings to the database.
        data.add_reading(time=reading_time, name='{0}'.format(sensor1Name), value=temp)
        data.add_reading(time=reading_time, name='{0}'.format(sensor2Name), value=touch)

        # Wait 2 minutes (120 seconds) and repeat.
        time.sleep(2.0)
finally:
    # Finally close the connection to the database when done.
    data.close()
