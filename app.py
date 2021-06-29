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
    opponent=data["opponent"]
    turnColor=data["turnColor"]
    winner=rules(board, 2 if turnColor == 1 else 1)  
    if winner!=0:
        return jsonify({
            "board": board,
            "winner": winner
        })

    newBoard=makeMove(board, opponent,turnColor)
    winner=rules(board, turnColor)

    return jsonify({
        "board": newBoard,
        "winner": winner
    })

def makeMove(board,opponent,turnColor):
    if opponent=="basic":
        newBoard=basic9_9(board, turnColor)
        return newBoard


    if opponent=="random":
        newBoard=random9_9(board,turnColor)
        return newBoard
    
    print("request missing opponent")
    raise Exception("request missing opponent")
    return board

def basic9_9(board,turnColor):
    time.sleep(1)

    opponentColor=2 if turnColor == 1 else 1
    
    opposingGroups=identifyGroups(board,opponentColor)
    # break if no groups. fix this when fix coloring
    
    # find moves that minimise opponent liberties
    libertyCount=1000000
    groupWithLeastLiberties=opposingGroups[0]
    for group in opposingGroups:
        if len(group[1])<libertyCount:
            groupWithLeastLiberties=group
            libertyCount=len(group[1])
    

    # prefer moves that maximise own liberties
    liberties=groupWithLeastLiberties[1]
    potentialMoveLibertyCount=-1
    newMove=(0,0)

    for tuple in liberties:
        potentialBoard=copy.deepcopy(board)
        potentialBoard[tuple[0]][tuple[1]]=turnColor
        potentialGroup=floodFill(tuple[0],tuple[1],potentialBoard,turnColor)
        potentialLibertySet=returnLibertiesSet(potentialGroup,potentialBoard)
        if len(potentialLibertySet)>potentialMoveLibertyCount:
            potentialMoveLibertyCount=len(potentialLibertySet)
            newMove=tuple
    
    board[newMove[0]][newMove[1]]=turnColor
    
    return board



def random9_9(board,turnColor):
    time.sleep(1)
    
    newBoard=board
    moveSuccesful=False
    while(not moveSuccesful):
        col=random.randint(0,8)
        row=random.randint(0,8)
        if(newBoard[col][row] == 0):
            newBoard[col][row] = turnColor
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
