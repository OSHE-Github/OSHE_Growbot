import os
import datetime
import smtplib
from email.message import EmailMessage

# Adds a timestamp to the filenames
reading_time = datetime.datetime.now()
sensors = reading_time.strftime('%m-%d-%Y') + '_sensors.csv'
sensorreadings = reading_time.strftime('%m-%d-%Y') + '_sensorreadings.csv'

print(sensors)
print(sensorreadings)
# os.rename('sensors.csv', sensors)
# os.rename('sensorreadings.csv', sensorreadings)


msg = EmailMessage()
msg["From"] = 'OSHETesting@gmail.com'
msg["Subject"] = reading_time.strftime('%m-%d-%Y') + 's files'
msg["To"] = 'wilsonh@mtu.edu'
msg.set_content("Here are the .csv files of the Growbot's databse tables from " + reading_time.strftime('%m-%d-%Y'))
msg.add_attachment(open('04-26-2020_sensors.csv', "r").read(), filename="04-26-2020_sensors.csv")
msg.add_attachment(open('04-26-2020_sensors.csv', "r").read(), filename="04-26-2020_sensorreadings.csv")

s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login('OSHETesting', 'opensource')
s.send_message(msg)
