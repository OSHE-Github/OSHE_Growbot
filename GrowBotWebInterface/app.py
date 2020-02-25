import os
from flask import Flask, render_template, flash, redirect, url_for, session, request, logging, send_from_directory, jsonify
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

@app.route('/interactive/')
def interactive():
	return render_template('interactive.html')

@app.route('/background_process')
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

@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                          'favicon.ico',mimetype='image/vnd.microsoft.icon')

@app.route('/calibrate')
def calibrate():
    calibrateODRIVE()
    return render_template('calibrate.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True) #host='0.0.0.0'
