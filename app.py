from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html', app_name="My Cool Flask App", message="This is rendered dynamically!")

