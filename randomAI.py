import random

def random9_9(board,turnColor):  
    newBoard=board
    newMove=[0,0]
    moveSuccesful=False
    while(not moveSuccesful):
        col=random.randint(0,8)
        row=random.randint(0,8)
        if(newBoard[col][row] == 0):
            newBoard[col][row] = turnColor
            newMove=[col, row]
            moveSuccesful=True

    return (newBoard, newMove)