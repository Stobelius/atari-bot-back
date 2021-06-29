import group_liberty_utilities as utils

def rules(board, lastTurnColor):
    if didColorWin(board, lastTurnColor):
        return lastTurnColor
    if didColorWin(board, 2 if lastTurnColor == 1 else 1):
        return 2 if lastTurnColor == 1 else 1
    return 0

def didColorWin(board, color):
    groups = utils.identifyGroups(board, 2 if color == 1 else 1)

    
    for g in groups:
        if len(g[1]) == 0:
            print("winner is "+str(color))
            return True
            

    return False