import copy

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