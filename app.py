import flask
from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return flask.render_template('index.html')


@app.route('/get_answer', methods=['POST'])
def get_answer():
    answer = [
        [1,1,1,2,2,2,3,3,3], [], [1,1,1,2,2,2,3,3,3],
        [], [], [],
        [], [], [],
    ]
    return {'answer': answer}


if __name__ == '__main__':
    app.run()
