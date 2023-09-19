from flask import Flask

app = Flask(__name__)


@app.route('/mega/')
def mega():
    print()
    return ''


if __name__ == '__main__':
    app.run()
