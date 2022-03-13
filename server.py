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


@app.route('/submit_form', methods=['POST', 'GET'])
def submit_form():
    """Send message."""
    if request.method == 'POST':
        data = request.form.to_dict()
        print(data)
        response = "Your message was sucessfully sent"
    else:
        response = "Your message not sent"
    return render_template('contact.html', response=response)
