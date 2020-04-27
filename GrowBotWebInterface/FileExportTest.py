import os
import datetime
import smtplib
from email.message import EmailMessage

# Adds a timestamp to the filenames
reading_time = datetime.datetime.now()
readDate = reading_time.strftime('%m-%d-%Y')
sensors = readDate + '_sensors.csv'
sensorreadings = readDate + '_sensorreadings.csv'

# Sends an email with .csv attachment
msg = EmailMessage()
msg["From"] = 'OSHETesting@gmail.com'
msg["Subject"] = readDate + ' *.csv files'
msg["To"] = 'wilsonh@mtu.edu'   # Put your email here
msg.set_content("Here are the .csv files of the Growbot's databse tables from " + readDate)
msg.add_attachment(open('sensors.csv', "r").read(), filename=sensors)
msg.add_attachment(open('sensorreadings.csv', "r").read(), filename=sensorreadings)

# Sends the email
s = smtplib.SMTP_SSL('smtp.gmail.com')
s.login('OSHETesting@gmail.com', 'opensource')  # Email I created and used for testing. Have to turn on support for less secure apps.
s.send_message(msg)
