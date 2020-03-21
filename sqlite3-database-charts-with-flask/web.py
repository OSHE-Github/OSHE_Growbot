from flask import Flask, render_template, request
import sqlite3
import json

app = Flask(__name__)


@app.route("/data.json")
def data():
    connection = sqlite3.connect("db.sqlite")
    cursor = connection.cursor()
    cursor.execute("SELECT 1000*timestamp, measure from measures")
    results = cursor.fetchall()
    print results
    return json.dumps(results)

@app.route("/graph")
def graph():
    return render_template('graph.html')


if __name__ == '__main__':
    app.run(
    debug=True,
    threaded=True,
    host='0.0.0.0'
)
