from flask import Flask
from flask import jsonify

app = Flask(__name__)


@app.route('/')
def hello():
    """print hello world for root directory"""
    print('From inside the hello() function')
    return 'Hello World...'


@app.rount('/echo')
def echo(name):
    """echo's the contents of the name query parameter to screen"""
    print(f"here's the query paramter: {name}")
    val = {"name-name": name}
    return jsonify(val)


if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8080, debug=True)
