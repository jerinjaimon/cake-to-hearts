from flask import Flask, render_template, url_for, send_from_directory
import os

app = Flask(__name__)


@app.route("/")
@app.route("/index.html")
def home_page():
    """Home page."""
    return render_template('index.html')


@app.route("/about.html")
def about_page():
    """About page."""
    return render_template('about.html')


@app.route("/services.html")
def service_page():
    """About page."""
    return render_template('services.html')


@app.route("/project.html")
def project_page():
    """About page."""
    return render_template('services.html')


@app.route("/contact.html")
def contact_page():
    """About page."""
    return render_template('contact.html')


@app.route("/components.html")
def component_page():
    """About page."""
    return render_template('components.html')
