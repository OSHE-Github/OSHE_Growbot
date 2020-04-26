import os
import datetime

# Adds a timestamp to the filenames
reading_time = datetime.datetime.now()
sensors = reading_time.strftime('%m/%d/%Y') + 'sensors.csv'
sensorreadings = reading_time.strftime('%m/%d/%Y') + 'sensorreadings.csv'
os.rename('sensors.csv', sensors)
os.rename('sensorreadings.csv', sensorreadings)
