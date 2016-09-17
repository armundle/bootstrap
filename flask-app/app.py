from flask import Flask, jsonify

import settings

app = Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    return jsonify('hello')


if __name__ == "__main__":
    app.run(debug=settings.DEBUG,
            port=int(settings.PORT))
