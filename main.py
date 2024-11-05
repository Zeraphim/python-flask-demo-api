from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/hello', methods=['GET'])
def hello():
    return jsonify({"text": "hello world"})

if __name__ == '__main__':
    app.run(debug=True, port=8080)