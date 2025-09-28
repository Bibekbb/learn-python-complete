def sum(a, b , c):
    return a+b+c

def printBoard(xStaete,zState):
    Zero = 'X' if xStaete[0] else ('O' if zState[0] else 0)
    One = 'X' if xStaete[1] else ('O' if zState[1] else 1)
    Two = 'X' if xStaete[2] else ('O' if zState[2] else 2)
    Three = 'X' if xStaete[3] else ('O' if zState[3] else 3)
    Four = 'X' if xStaete[4] else ('O' if zState[4] else 4)
    Five = 'X' if xStaete[5] else ('O' if zState[5] else 5)
    Six = 'X' if xStaete[6] else ('O' if zState[6] else 6)
    Seven = 'X' if xStaete[7] else ('O' if zState[7] else 7)
    Eight= 'X' if xStaete[8] else ('O' if zState[8] else 8)
    print(f" {Zero}| {One} | {Two} ")
    print(f"--|---|---")
    print(f"{Three} | {Four} | {Five} ")
    print(f"--|---|---")
    print(f"{Six} | {Seven} | {Eight} ")

def checkWin(xState, zState):
    wins = [[0,1,2], [3,4,5],[6,7,8],[0,3,6],[1,4,7],[2,5,8],[0,4,8],[2,4,6]]
    for win in wins:
        if (sum(xState[win[0]],xState[win[1]],xState[win[2]]) == 3):
            print("X won the Match.")
            return 1
        if (sum(zState[win[0]],zState[win[1]],zState[win[2]] == 3)):
            print("O Won the Match.")
            return 0
    return -1

if __name__ == "__main__":
    xState = [0,0,0,0,0,0,0,0,0]
    zState = [0,0,0,0,0,0,0,0,0]
    turn = 1 #1 for x and 0 for O
    print("welcome to Tic Tac Toe")
    while(True):
        printBoard(xState,zState)
        if(turn == 1):
            print("X's Chance")
            Value = int(input("Please enter a value: "))
            xState[Value] = 1
        else:
            print("O's Chance")
            Value = int(input("Please enter a value: "))
            zState[Value] = 1
        cwin = checkWin(xState, zState)
        if(cwin != -1):
            print("Game Over")
            break
        
        turn = 1- turn
        