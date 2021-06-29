from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import time
import basicAI
import randomAI
import rules



app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['POST'])
def main():
    data=json.loads(request.data)
    board = data["board"]
    print(data["test"])
    opponent=data["opponent"]
    turnColor=data["turnColor"]
    winner=rules.rules(board, 2 if turnColor == 1 else 1)  
    if winner!=0:
        return jsonify({
            "board": board,
            "winner": winner
        })

    newBoard=makeMove(board, opponent,turnColor)
    winner=rules.rules(board, turnColor)

    return jsonify({
        "board": newBoard,
        "winner": winner
    })

def makeMove(board,opponent,turnColor):
    time.sleep(1)

    if opponent=="basic":
        newBoard=basicAI.basic9_9(board, turnColor)
        return newBoard


    if opponent=="random":
        newBoard=randomAI.random9_9(board,turnColor)
        return newBoard
    
    return board




