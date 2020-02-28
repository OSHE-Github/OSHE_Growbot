from flask import Flask,render_template,url_for,request,redirect, make_response
import random
import json
from time import time
from random import random
from flask import Flask, render_template, make_response
from gettemps import getTemp

app = Flask(__name__)


# Defines the home page
@app.route('/', methods=["GET", "POST"])
def main():
    return render_template('index.html')


# Defines the data webpage (not seen by the user)
@app.route('/data', methods=["GET", "POST"])
def data():
    # Data Format
    # [TIME, Temperature, Moisture]

    time.sleep(1)
    Temperature = getTemp()
    Moisture = random() * 55

    data = [time() * 1000, Temperature, Moisture]

    response = make_response(json.dumps(data))

    response.content_type = 'application/json'

    return response


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
