from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import time

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['POST'])
def hello_world():
    data=json.loads(request.data)
    print(data["test"])
    newdata=makeMove(data["board"])
    return jsonify({"board": newdata})

def makeMove(board):
    newboard=random9_9move(board)
    return newboard

def random9_9move(board):
    time.sleep(1)
    
    newBoard=board
    moveSuccesful=False
    while(not moveSuccesful):
        col=random.randint(0,8)
        row=random.randint(0,8)
        if(newBoard[col][row] == 0):
            newBoard[col][row] = 2
            moveSuccesful=True

    return newBoard

def rules(board, lastTurnColor):
    if didColorWin(board, lastTurnColor):
        return lastTurnColor
    if didColorWin(board, lastTurnColor == 1 ? 2 : 1):
        return lastTurnColor
    return

def didColorWin(board, color):
    groups = identifyGroups(color == 1 ? 2 : 1)
    
    for g in groups:
        if len(g[1]) = 0:
            return True

    return False

def identifyGroups(board, color):
    groups = {}
    checkedIntersections = {}
    for col in range(len(board)):
        for row in range(len(col)):
            if board[col][row] == color && not ((col, row) in checkedIntersections)):
                #finish from paper later

                
                
def returnAdjacentCoords(board
