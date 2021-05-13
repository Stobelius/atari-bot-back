from flask import Flask,request
import json

app = Flask(__name__)

@app.route("/test", methods=['POST'])
def hello_world():
    data=json.loads(request.data)
    print(data["test"])
    newdata=makeMove(data["board"])
    return {"board": newdata} 

def makeMove(board):
    newboard=board
    return newboard
