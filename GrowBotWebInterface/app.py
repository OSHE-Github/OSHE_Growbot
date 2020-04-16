#Wilson Holmes
#Open Source Hardware Enterprise
#Growbot
#Created: 2020/02/23
#Last Modified: 2020/04/15
#Description: Flask app that is the front end of the Browbot Web UI

# These imports are in the standard python3 library quiver, did not need to install these ones through pip
import os
import time   # might need to "from time import time" instead
from random import random
import sqlite3
import csv
import atexit
from glob import glob; from os.path import expanduser
import pandas as pd
# Flask
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, send_from_directory, jsonify, make_response, flash, Response
# WTForms
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
# Flask-Admin
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
# APScheduler
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.triggers.interval import IntervalTrigger
# Raspberry Pi camera module (requires picamera package)
from camera_pi import Camera
# model.py file that defines the databse and its behavior using the peewee orm
import model


app = Flask(__name__)
app.config['SECRET_KEY'] = 'OSHE'
# Add the sensor data model to the app config so templates can reach it and query
# the sensors & readings.
app.config['MODEL'] = model.SensorData()


# Add an admin view for the Peewee ORM-based sensor and sensor reading models.
admin = Admin(app, name='Growbot Sensors', template_mode='bootstrap3', url='/admin')
admin.add_view(ModelView(model.Sensor))
admin.add_view(ModelView(model.SensorReading))


def db2csv():
    conn = sqlite3.connect(glob(expanduser('growbot.db'))[0])
    cursor = conn.cursor()
    sensors = pd.read_sql('SELECT * FROM sensor' ,conn)
    sensorreadings = pd.read_sql('SELECT * FROM sensorreading' ,conn)
    sensors.to_csv('sensors.csv', index=False)
    sensorreadings.to_csv('sensorreadings.csv', index=False)


# create schedule for printing time
scheduler = BackgroundScheduler()
scheduler.start()
scheduler.add_job(
    func=db2csv,
    trigger=IntervalTrigger(hours=24),
    id='db2csv_job',
    name='clear and save db to csv every day',
    replace_existing=True)
# Shut down the scheduler when exiting the app
atexit.register(lambda: scheduler.shutdown())


# Home Page
@app.route('/')
def index():
    return render_template('home.html')


# About page for project
@app.route('/about')
def about():
    # x_Accel, y_Accel = readXYAccel()
    # if (x_Accel > 5 or y_Accel > 5):
    #     flash("This is an alert! Your Robot may have tipped over!")
    return render_template('about.html')


def gen(camera):
    """Video streaming generator function."""
    while True:
        frame = camera.get_frame()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame + b'\r\n')


@app.route('/video_feed')
def video_feed():
    """Video streaming route. Put this in the src attribute of an img tag."""
    return Response(gen(Camera()),
                    mimetype='multipart/x-mixed-replace; boundary=frame')


# GrowCam page, maybe make this openCV sometime in the future for pest identification
@app.route('/growcam')
def growcam():
    return render_template('growcam.html')


# # Page with a simple calculator done as a test of how to parse input and output
# # from the website to a python variable
# @app.route('/calculator', methods=['GET', 'POST'])
# def calculator():
#     if request.method == 'GET':
#         return render_template('calculator.html')
#     elif request.method == 'POST':
#         expression = request.form.get('expression')
#         result = eval(expression)
#         return render_template('calculator.html', result = result)


# Adds the OSHE logo icon to the browser tab
@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static/images'), 'favicon.ico',mimetype='image/vnd.microsoft.icon')


# Hopefully this url can be used to trigger a calibration python script on the robot
@app.route('/calibrate')
def calibrate():
    calibrateODRIVE()
    return render_template('calibrate.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, threaded=True)
