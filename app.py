from flask import Flask, request, jsonify
from flask_cors import CORS
import json
import random
import time
import copy

app = Flask(__name__)
CORS(app)

@app.route("/test", methods=['POST'])
def main():
    data=json.loads(request.data)
    board = data["board"]
    print(data["test"])
    winner=rules(board, 1)  
    if winner!=0:
        return jsonify({
            "board": board,
            "winner": winner
        })

    newBoard=makeMove(board)
    winner=rules(board, 2)

    return jsonify({
        "board": newBoard,
        "winner": winner
    })

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
        return 2 if lastTurnColor == 1 else 1
    return 0

def didColorWin(board, color):
    groups = identifyGroups(board, 2 if color == 1 else 1)

    
    for g in groups:
        if len(g[1]) == 0:
            print("winner is "+str(color))
            return True
            

    return False

def identifyGroups(board, color):
    groups = []
    groupsAndLiberties = []
    iteratedBoard = copy.deepcopy(board)
    #print("this is the board" + str(board))
    for col in range(len(board)):
        for row in range(len(board[col])):
            if iteratedBoard[col][row] == color:
                groups.append(floodFill(col, row, iteratedBoard, color))

    for group in groups:
        groupsAndLiberties.append((group,returnLibertiesSet(group,board)))

    return groupsAndLiberties

def returnLibertiesSet(group, board):
    libertySet = set()
    returnSet = set()

    for tuple in group:
        libertySet=libertySet.union(libertySet,returnAdjacentCoords(tuple[0], tuple[1]))

    for tuple in libertySet:
        if board[tuple[0]][tuple[1]]==0:
            returnSet.add(tuple)

    return returnSet        

def floodFill(col, row, iteratedBoard, color):
    group = set()

    def floodFillHelper(col, row, iteratedBoard, color):
        if iteratedBoard[col][row] != color:
            return

        group.add((col, row))
        iteratedBoard[col][row] = 3

        adjacentIntersections = returnAdjacentCoords(col, row)
        for i in adjacentIntersections:
            floodFillHelper(i[0], i[1], iteratedBoard, color)

    floodFillHelper(col, row, iteratedBoard, color)

    #if len(group):
        #print(group)
    return group
                
def returnAdjacentCoords(col, row):
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
