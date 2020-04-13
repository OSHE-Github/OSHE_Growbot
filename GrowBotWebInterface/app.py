import os
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, send_from_directory, jsonify, make_response, flash
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
# from testfunctions import hellonameloop
from odrive import calibrate as calibrateODRIVE
import random
import json
from time import time
from random import random
import sqlite3
from flask_admin import Admin
from flask_admin.contrib.peewee import ModelView
# from nineDofSensor import readXYAccel

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


# This chunk of commented out code was a test of graphing live data, which
# I no longer thing we will be doing on this project as we will most likely
# not need better than even perhaps 10 minute precision, so I may just have
# the webpage auto refresh every 10 minutes instead.

# # Defines the sensors page
# @app.route('/sensors', methods=["GET", "POST"])
# def main():
#     return render_template('sensors.html')
#
#
# # Defines the data webpage (not seen by the user)
# @app.route('/data', methods=["GET", "POST"])
# def data():
#     # Data Format
#     # [TIME, Temperature, Moisture]
#
#     Temperature = getTemp()
#     Moisture = random() * 55
#
#     data = [time() * 1000, Temperature, Moisture]
#
#     response = make_response(json.dumps(data))
#
#     response.content_type = 'application/json'
#
#     return response

# Javascript testing
@app.route('/interactive')
def interactive():
	return render_template('interactive.html')

# More Javascript testing
@app.route('/_background_process')
def background_process():
	lang = request.args.get('proglang', 0, type=str)
	if lang.lower() == 'python':
		return jsonify(result='You are wise')
	else:
		return jsonify(result='Try again.')


# @app.route('/background_process')
# def background_process():
# 	try:
# 		lang = request.args.get('proglang', 0, type=str)
# 		if lang.lower() == 'python':
# 			return jsonify(result='You are wise')
# 		else:
# 			return jsonify(result='Try again.')
# 	except Exception as e:
# 		return str(e)

# Page with a simple calculator done as a test of how to parse input and output
# from the website to a python variable
@app.route('/calculator', methods=['GET', 'POST'])
def calculator():
    if request.method == 'GET':
        return render_template('calculator.html')
    elif request.method == 'POST':
        expression = request.form.get('expression')
        result = eval(expression)
        return render_template('calculator.html', result = result)


@app.route('/', methods=['GET', 'POST'])
def test():
    if request.method == 'POST':
        name = request.form['NAME']
        i = request.form['I']
        result = hellonameloop(name, i)
        return render_template('test.html', result = result)
    else:
        return render_template('test.html')

@app.route('/test')
def test2():
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

# Test of graphing dummy data to the webiste from a sqlite3 database
@app.route("/data.json")
def data():
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT 1000*timestamp, measure from measures")
    results = cursor.fetchall()
    print(results)
    return json.dumps(results)

# Actual graph webpage on the website.
@app.route('/graphs')
def graphs():
    return render_template('graphs.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True)
