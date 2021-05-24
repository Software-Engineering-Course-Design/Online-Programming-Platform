#实现api，并且演示api的get post，以及他的request里的param，query，body

from flask import Flask
app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello, World!'