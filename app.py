from flask import Flask
import os
import numpy as np

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    print("teste")


if __name__ == '__main__':
    app.run(debug=True)