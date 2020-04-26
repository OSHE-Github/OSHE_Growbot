#Wilson Holmes
#Open Source Hardware Enterprise
#Growbot
#Created: 2020/04/16
#Last Modified: 2020/04/16
#Description: This is a template file to be used when adding new sensors to the gowbot. The website pulls data from both the sensor table and the sensorreading table in the sqlite3 database to create the graphs. So in order to add a new sensor you will need to get the data from the sensor, populate the sensor database with a name and unit for every reading, and put the datetime, sensor name, and value of the reading in the sensorreading table of the database. e.g. "Generic-Sensor Temperature" for the name and "°C" for the units in the sensor table; and "datetime" for the date, "Generic-Sensor Temperature" for the name, and a numer for the value in the sensorreading table. Look through this file and its comments to follow how the methods imported from model.py are used to achieve this. If more reference is needed, SoilSensorReadOnly.py is in this same directory, and is just this file edited for use with an adafruit_circuitpython_seesaw sensor. One last thing to note (if you are still indeed reading this) is that you will need to have a sensor entry for every value that you wish to store. That is why I formatted the sensor names like "Generic-Sensor Temperature" as (for many sensors) they can read multiple values in, so you would need to add another sensor to the database named "Generic-Sensor [name of other thing being measure e.g. Moisture]" to be able to properly graph and store the data.

import time
import datetime

# Imports for the SGP30 sensor
import board
import busio
import adafruit_sgp30

import model # For saving the sensor data to the database


# Create an instance of our data model access layer object.
# This object takes care of all the Peewee ORM and DB access so our code in this
# file is very simple and just calls function on the model access layer object.
data = model.SensorData()

# Define which sensors we expect to be connected to the Pi and their units.
sensor1Name = 'SGP30 eCO2'
sensor1Units = 'ppm'
sensor2Name = 'SGP30 TVOC'
sensor2Units = 'ppb'

# If there are no prexisting entrys into the sensor table in the databse with these exact names and units, then a new entry will be created in the table.
data.define_sensor(sensor1Name, sensor1Units)
data.define_sensor(sensor2Name, sensor2Units)

i2c = busio.I2C(board.SCL, board.SDA, frequency=100000)

# Create library object on our I2C port
sgp30 = adafruit_sgp30.Adafruit_SGP30(i2c)

print("SGP30 serial #", [hex(i) for i in sgp30.serial])

sgp30.iaq_init()
sgp30.set_iaq_baseline(0x8973, 0x8AAE)

elapsed_sec = 0


try:
    # Loop to continually add data to the database.
    while True:
        # Get the current time for this batch of sensor readings.
        reading_time = datetime.datetime.now()

        # Read sensor eCO2
        eCO2 = sgp30.eCO2;

        # Read sensor TVOC
        TVOC = sgp30.TVOC;

        # Print out sensor values
        print("Reading Sensor -> SGP30: eCO2: " + str(eCO2) + " ppm,  TVOC: " + str(TVOC) + " ppb")

        time.sleep(1)
        elapsed_sec += 1
        if elapsed_sec > 10:
            elapsed_sec = 0
            print("**** Baseline values: eCO2 = 0x%x, TVOC = 0x%x" % (sgp30.baseline_eCO2, sgp30.baseline_TVOC))

        # Add the sensor readings to the database.
        data.add_reading(time=reading_time, name='{0}'.format(sensor1Name), value=eCO2)
        data.add_reading(time=reading_time, name='{0}'.format(sensor2Name), value=TVOC)

        # Wait 60 seconds and repeat. set this to something more reasonable once you are done testing. The Website is currently set up to show 120 points on each graph, so if you are storing a sensor value every 2 minutes (120 seconds) into the database, then your graphs will show you a view of the last 4 hours.
        time.sleep(60.0)
finally:
    # Finally close the connection to the database when done.
    data.close()
