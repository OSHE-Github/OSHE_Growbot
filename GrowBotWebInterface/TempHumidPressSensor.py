import time
import datetime

import model # For saving the sensor data to the database

import board
import busio
import adafruit_bme280

# Create an instance of our data model access layer object.
# This object takes care of all the Peewee ORM and DB access so our code in this
# file is very simple and just calls function on the model access layer object.
data = model.SensorData()

# Define which sensors we expect to be connected to the Pi.
sensor1Name = 'BME280 Temperature'
sensor1Units = '°C'
sensor2Name = 'BME280 Humidity'
sensor2Units = '%'
sensor3Name = 'BME280 Pressure'
sensor3Units = 'hPa'
sensor4Name = 'BME280 Altitude'
sensor4Units = 'Meters'
data.define_sensor(sensor1Name, sensor1Units)
data.define_sensor(sensor2Name, sensor2Units)
data.define_sensor(sensor3Name, sensor3Units)
data.define_sensor(sensor4Name, sensor4Units)

# Create library object using our Bus I2C port
i2c = busio.I2C(board.SCL, board.SDA)
bme280 = adafruit_bme280.Adafruit_BME280_I2C(i2c)

# OR create library object using our Bus SPI port
# spi = busio.SPI(board.SCK, board.MOSI, board.MISO)
# bme_cs = digitalio.DigitalInOut(board.D10)
# bme280 = adafruit_bme280.Adafruit_BME280_SPI(spi, bme_cs)

# change this to match the location's pressure (hPa) at sea level
bme280.sea_level_pressure = 1013.25

while True:
    # Get the current time for this batch of sensor readings.
    reading_time = datetime.datetime.now()

    # read in all sensor values
    temperature = bme280.temperature
    humidity = bme280.humidity
    pressure = bme280.pressure
    altitude = bme280.altitude

    # Print out sensor values
    print("\nReading Sensor -> SeeSaw Soil:"
    print(" Temperature: %0.1f °C," % bme280.temperature)
    print(" Humidity: %0.1f %%," % bme280.humidity)
    print(" Pressure: %0.1f hPa," % bme280.pressure)
    print(" Altitude = %0.2f Meters" % bme280.altitude)

    # Add the sensor readings to the database.
    data.add_reading(time=reading_time, name='{0}'.format(sensor1Name), value=temperature)
    data.add_reading(time=reading_time, name='{0}'.format(sensor2Name), value=humidity)
    data.add_reading(time=reading_time, name='{0}'.format(sensor3Name), value=pressure)
    data.add_reading(time=reading_time, name='{0}'.format(sensor4Name), value=altitude)

    # Wait 4 seconds and repeat.
    time.sleep(4.0)

finally:
    # Finally close the connection to the database when done.
    data.close()
