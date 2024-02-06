#!/usr/bin/env python3

from flask import Flask
'''setup a basic Flask app
'''

app = Flask(__name__)
@app = route('/')

def home():
    return render_template("0-index.html",)

if __name__ == "__main__":
    app.run(debug=True)
