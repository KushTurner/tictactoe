# global variables

gameTable = ['-', '-', '-',
             '-', '-', '-',
             '-', '-', '-']

score = {'X': 0,
         'O': 0}
currentPlayer = 'X'
winner = None
gameRunning = True
plr1 = None
plr2 = None


# creating board


def printBoard(board):
    # print('-------------------')
    print('[ ' + board[0] + ' ] ' + ' [ ' + board[1] + ' ] ' + ' [ ' + board[2] + ' ]')
    # print('-------------------')
    print('[ ' + board[3] + ' ] ' + ' [ ' + board[4] + ' ] ' + ' [ ' + board[5] + ' ]')
    # print('-------------------')
    print('[ ' + board[6] + ' ] ' + ' [ ' + board[7] + ' ] ' + ' [ ' + board[8] + ' ]')
    # print('-------------------')


# Win conditions


def checkHorizontal():
    global winner
    if gameTable[0] == gameTable[1] == gameTable[2] and gameTable[1] != '-':
        winner = gameTable[0]
        return True
    elif gameTable[3] == gameTable[4] == gameTable[5] and gameTable[4] != '-':
        winner = gameTable[3]
        return True
    elif gameTable[6] == gameTable[7] == gameTable[8] and gameTable[7] != '-':
        winner = gameTable[6]
        return True


def checkVertical():
    global winner
    if gameTable[0] == gameTable[3] == gameTable[6] and gameTable[3] != '-':
        winner = gameTable[0]
        return True
    elif gameTable[1] == gameTable[4] == gameTable[7] and gameTable[4] != '-':
        winner = gameTable[1]
        return True
    elif gameTable[2] == gameTable[5] == gameTable[8] and gameTable[5] != '-':
        winner = gameTable[2]
        return True


def checkDiagonal():
    global winner
    if gameTable[0] == gameTable[4] == gameTable[8] and gameTable[4] != '-':
        winner = gameTable[0]
        return True
    elif gameTable[2] == gameTable[4] == gameTable[6] and gameTable[4] != '-':
        winner = gameTable[2]
        return True


# game functionality


def createPlayer():
    global plr1
    global plr2
    plr = str(input('What is your name? '))
    if plr1 is None:
        plr1 = plr
    else:
        plr2 = plr



def askInput():
    global gameRunning
    inp = int(input('Pick a spot: '))
    if 1 <= inp <= 9 and gameTable[inp - 1] == '-':
        gameTable[inp - 1] = currentPlayer
    else:
        print('Invalid spot')
        askInput()


def switchPlayer():
    global currentPlayer
    if currentPlayer == 'X':
        currentPlayer = 'O'
        print(plr2 + ' ' + currentPlayer)
    else:
        currentPlayer = 'X'
        print(plr1 + ' ' + currentPlayer)


def playAgain(table):
    global gameRunning
    answer = str(input('Play again? '))
    if str.lower(answer) == 'yes' or str.lower(answer) == 'y':
        for i in range(len(table)):
            table[i] = '-'
    else:
        gameRunning = False


def checkWin():
    global gameRunning
    global winner
    global score
    global currentPlayer
    global plr1
    global plr2
    if checkDiagonal() or checkVertical() or checkHorizontal() is True:
        if winner == 'X':
            wnr = plr1
        else:
            wnr = plr2
        printBoard(gameTable)
        print('The winner is {} ({})'.format(winner, wnr))
        score[winner] += 1
        showScore(score)
        playAgain(gameTable)


def checkTie():
    global score
    if '-' not in gameTable:
        printBoard(gameTable)
        print('It is a tie')
        showScore(score)
        playAgain(gameTable)


def showScore(scoreDict):
    print(plr1 + ' X: ' + str(scoreDict['X']))
    print(plr2 + ' O: ' + str(scoreDict['O']))


# game running

createPlayer()
createPlayer()

while gameRunning:
    printBoard(gameTable)
    askInput()
    checkWin()
    checkTie()
    switchPlayer()
