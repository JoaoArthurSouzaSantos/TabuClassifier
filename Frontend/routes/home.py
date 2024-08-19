from flask import Flask, Blueprint

app = Blueprint(__name__, url_prefix='home')


@app.route('/', methods=['GET', 'POST'])
def index():
    return "Home"

if __name__ == '__main__':
    app.run(debug=True)
