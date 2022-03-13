from flask import Flask, render_template, url_for, send_from_directory
import os

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
