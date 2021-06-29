import group_liberty_utilities as utils
import copy
import randomAI

def basic9_9(board,turnColor):
    opponentColor=2 if turnColor == 1 else 1
    
    opposingGroups=utils.identifyGroups(board,opponentColor)
    
    if len(opposingGroups)==0:
        if(board[4][4]==0):
            board[4][4]=turnColor
            return board
        return randomAI.random9_9(board,turnColor)
    
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
        potentialGroup=utils.floodFill(tuple[0],tuple[1],potentialBoard,turnColor)
        potentialLibertySet=utils.returnLibertiesSet(potentialGroup,potentialBoard)
        if len(potentialLibertySet)>potentialMoveLibertyCount:
            potentialMoveLibertyCount=len(potentialLibertySet)
            newMove=tuple
    
    board[newMove[0]][newMove[1]]=turnColor
    
    return board
