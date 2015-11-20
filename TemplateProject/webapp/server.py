'''
@author: besil
'''
from flask import Flask
from flask import render_template
import json

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("index.html")

@app.route("/example/data")
def example_rest():
    return json.dumps({"example": "data"})

@app.route("/favicon.ico")
def favicon():
    return "Favicon"
    
if __name__ == '__main__':
    app.debug = True
    port = 8080
    #host = "0.0.0.0"
    host = "127.0.0.1"
    app.run(host=host, port=port)
