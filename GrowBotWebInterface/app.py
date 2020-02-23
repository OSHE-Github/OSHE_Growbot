from flask import Flask, render_template, flash, redirect, url_for, session, request, logging
from wtforms import Form, StringField, TextAreaField, PasswordField, validators
from testfunctions import hellonameloop
from odrive import calibrate as calibrateODRIVE

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('home.html')

@app.route('/about')
def about():
    return render_template('about.html')

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

#comment

@app.route('/calibrate')
def calibrate():
    calibrateODRIVE()
    return render_template('calibrate.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) #host='0.0.0.0'
