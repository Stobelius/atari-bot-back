import group_liberty_utilities as utils
import copy

def evalAI1_9_9(board,turnColor):
    boardSize = 9
    opponentColor=2 if turnColor == 1 else 1
    
    bestCandidate=(0, 0)
    bestScore= -100000
    for col in range(boardSize):
        for row in range(boardSize):
            if(board[col][row] == 0):
                potentialBoard = copy.deepcopy(board)
                potentialBoard[col][row] = turnColor
                newScore = evaluation(potentialBoard, turnColor)
                # pick left-uppest instead of random if same evaluation
                if(newScore > bestScore):
                    bestCandidate = (col, row)
                    bestScore = newScore
    
    board[bestCandidate[0]][bestCandidate[1]] = turnColor
    return (board, [bestCandidate[0], bestCandidate[1]])

def evaluation(board, lastColorToPlay):
    boardSize = 9


    opponentColor=2 if lastColorToPlay == 1 else 1
    ownGroups=utils.identifyGroups(board, lastColorToPlay)
    opposingGroups=utils.identifyGroups(board, opponentColor)
    evalNumber = 0

    # victory and defeat
    if(utils.didColorWin(board, lastColorToPlay)):
        evalNumber += 1000
    if(utils.didColorWin(board, opponentColor)):
        evalNumber -= 500

    # stones in atari
    captureThreats=set()
    for group in opposingGroups:
        if(len(group[1]) == 1):
            captureThreats=captureThreats.union(group[1])
    evalNumber += len(captureThreats)*20

    ownCaptureThreats=set()
    for group in ownGroups:
        if(len(group[1]) == 1):
            ownCaptureThreats=ownCaptureThreats.union(group[1])
    evalNumber -= len(ownCaptureThreats)*50

    # penalty for many groups
    evalNumber -= len(ownGroups)*3

    # penalty for each enemy liberty and bonus for each own liberty. Weighted to value first liberties more
    for group in opposingGroups:
        evalNumber -= harmonicSum(len(group[1]))
    for group in ownGroups:
        evalNumber += harmonicSum(len(group[1]))

    # penalty for stones in corners, edge and second line
    for col in range(boardSize):
        for row in range(boardSize):
            if(board[col][row] == lastColorToPlay):
                if (col == 0 or col == boardSize -1) and (row == 0 or row == boardSize -1):
                    evalNumber -= 5
                elif (col == 0 or col == boardSize -1 or row == 0 or row == boardSize -1):
                    evalNumber -= 2
                elif (col == 1 or col == boardSize -2 or row == 1 or row == boardSize -2):
                    evalNumber -=0.5

    return evalNumber

def harmonicSum(naturalNum):    
    returnVal=0
    for i in range(1, naturalNum + 1):
        returnVal += 1/i
    return returnVal