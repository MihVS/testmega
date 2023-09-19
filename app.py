from flask import Flask, request, Response

app = Flask(__name__)


@app.route('/mega', methods=['GET'])
def mega():
    print(request.args.to_dict())
    return Response(status="200 OK")


if __name__ == '__main__':
    app.run()
