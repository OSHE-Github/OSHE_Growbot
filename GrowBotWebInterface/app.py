#Wilson Holmes
#Open Source Hardware Enterprise
#Growbot
#Created: 2020/02/23
#Last Modified: 2020/04/15
#Description: Flask app that is the front end of the Browbot Web UI


from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, send_from_directory, jsonify, make_response, flash
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from time import time
from random import random
import sqlite3
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView


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


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        name = request.form['NAME']
        i = request.form['I']
        result = hellonameloop(name, i)
        return render_template('test.html', result = result)
    else:
        return render_template('test.html')


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
    app.run(host='0.0.0.0', debug=True)
