from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hola mundo desde Flask en Docker!"  

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
