from flask import Flask

app = Flask(__name__)


@app.route('/')
def inicio():
    return 'teste'


if __name__ == '__main__':
    app.run()
