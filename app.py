from flask import Flask, request, jsonify
from flask_cors import CORS
import json

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['POST'])
def hello_world():
    data=json.loads(request.data)
    print(data["test"])
    newdata=makeMove(data["board"])
    return jsonify({"board": newdata})

def makeMove(board):
    newboard=board
    return newboard
