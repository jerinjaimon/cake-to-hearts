"""Cake to Hearts Server Code.

Powered by: Python Flask
"""
import csv
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home_page():
    """Home page."""
    return render_template('index.html')


@app.route("/<page>")
def load_page(page):
    """About page."""
    return render_template(page)


@app.route("/project.html")
def project_page():
    """About page."""
    return render_template('services.html')


def write_data_to_csv(data, filename='database.csv'):
    """Write data to file."""
    with open(filename, encoding='UTF-8', mode='a', newline='') as file:
        csv_writer = csv.writer(file, delimiter=',')
        csv_writer.writerow(data.values())


@ app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Send message."""
    if request.method == 'POST':
        data = request.form.to_dict()
        write_data_to_csv(data)
        response = "Your message was sucessfully sent"
    else:
        response = "Your message not sent"
    return render_template('contact.html', response=response)
