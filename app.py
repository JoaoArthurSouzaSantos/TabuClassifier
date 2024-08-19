from flask import Flask
import os
import numpy as np
from Frontend.routes import home

app = Flask(__name__)
app.register_blueprint(home)

@app.route('/', methods=['GET', 'POST'])
def index():
    return "Home"

if __name__ == '__main__':
    app.run(debug=True)
