#color
print("\033[1;33;40m\n")

#timer
import time
def time_convert(sec):
  mins = sec // 60
  sec = sec % 60
  hours = mins // 60
  mins = mins % 60
  print("Game_time = {0}:{1}:{2}".format(int(hours),int(mins),sec))
input("Press Enter to start")
start_time = time.time()

import random
score=0

board = ["-","-","-",
         "-","-","-",
         "-","-","-"]
currentmove = "X"
Winner = True
gamerunning= True


def printboard(values):
    print("\n")
    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[0], values[1], values[2]))
    print('\t_____|_____|_____')

    print("\t     |     |")
    print("\t  {}  |  {}  |  {}".format(values[3], values[4], values[5]))
    print('\t_____|_____|_____')

    print("\t     |     |")

    print("\t  {}  |  {}  |  {}".format(values[6], values[7], values[8]))
    print("\t     |     |")
    print("\n")


#player input
def playerInput(board):
    myvar= int(input("Enter a number 1-9:"))
    if myvar >= 1 and myvar <= 9 and board[myvar-1] =="-":
        board[myvar-1] = currentmove
    else:
        print("Player 2 has taken this spot:")

#check for win or tie
def checkHorizontle(board):
    global winner
    if board[0] == board[1] == board[2] and board[1] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkRow(board):
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True

def checkDiagonal(board):
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board [6] and board[2] != "-":
        winner = board[2]
        return True

def checkTie(board):
    global gamerunning
    if "-" not in board:
        printboard(board)
        print("It is a Tie!")
        gamerunning = False

def checkWin():
    global gamerunning
    if checkDiagonal(board) or checkHorizontle(board) or checkRow(board):
        print(f"The winner is {winner}")
        gamerunning = False

#color
print("\033[1;35;40m\n")

#switch player
def switchplayer():
    global currentmove
    if currentmove == "X":
        currentmove = "0"
    else:
        currentmove = "X"

#computer
def computer(board):
    while currentmove == "0":
        position = random.randint(0,8)
        if board[position] == "-":
            board[position] = "0"
            switchplayer()



while gamerunning:
    printboard(board)
    playerInput(board)
    checkWin()
    checkTie(board)
    switchplayer()
    computer(board)
    checkWin()
    checkTie(board)

#color
print("\033[1;32;40m\n")

#Score
score=score+1
print("Your current score is", score)

#color
print("\033[1;36;40m\n")

#end timer
input("Press Enter to stop and get time")
end_time = time.time()
game_time = end_time - start_time
time_convert(game_time)

