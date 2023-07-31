import os
from flask import Flask, render_template
from flask_cors import CORS

app = Flask(__name__, static_folder='static')
app.debug = True


@app.route('/')
def home():
    return render_template('sample_view.htm')


@app.route('/<path:path>')
def serve_htm(path):
    return render_template(path)


if __name__ == '__main__':
    app.jinja_env.auto_reload = True
    app.config['TEMPLATES_AUTO_RELOAD'] = True
    app.run(port=5000)
