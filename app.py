from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import time
import copy

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['POST'])
def hello_world():
    data=json.loads(request.data)
    board = data["board"]
    print(data["test"])
    rules(board, 1)
    newBoard=makeMove(board)
    rules(board, 2)
    return jsonify({"board": newBoard})

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
    if didColorWin(board, 2 if lastTurnColor == 1 else 1):
        return lastTurnColor
    return

def didColorWin(board, color):
    groups = identifyGroups(board, 2 if color == 1 else 1)

    print(str(groups))
    
    #for g in groups:
    #    if len(g[1]) == 0:
    #        return True

    return False

def identifyGroups(board, color):
    groups = set()
    iteratedBoard = copy.deepcopy(board)
    #print("this is the board" + str(board))
    for col in range(len(board)):
        for row in range(len(board[col])):
            if iteratedBoard[col][row] == color:
                groups.add(floodFill(col, row, iteratedBoard, color))

def floodFill(col, row, iteratedBoard, color):
    group = set()

    def floodFillHelper(col, row, iteratedBoard, color):
        if iteratedBoard[col][row] != color:
            return

        group.add((col, row))
        iteratedBoard[col][row] = 3

        adjacentIntersections = returnAdjacentCoords(col, row, iteratedBoard)
        for i in adjacentIntersections:
            floodFillHelper(i[0], i[1], iteratedBoard, color)

    floodFillHelper(col, row, iteratedBoard, color)

    if len(group):
        print(group)
    return
                
def returnAdjacentCoords(col, row, board):
    returnSet = set()
    if row < 8:
        returnSet.add((col, row + 1))
    if row > 0:
        returnSet.add((col, row - 1))
    if col < 8:
        returnSet.add((col + 1, row))
    if col > 0:
        returnSet.add((col -1, row))
    return returnSet
