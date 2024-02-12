def printtictactoetable(tictactoetable):
    print(tictactoetable[1] + '|' + tictactoetable[2] + '|' + tictactoetable[3])
    print('-+-+-')
    print(tictactoetable[4] + '|' + tictactoetable[5] + '|' + tictactoetable[6])
    print('-+-+-')
    print(tictactoetable[7] + '|' + tictactoetable[8] + '|' + tictactoetable[9])
    print("\n")
    
def spaceIsFree(position):
    if tictactoetable[position] == ' ':
        return True
    else:
        return False
        
def insertLetter(letter, position):
    if spaceIsFree(position):
        tictactoetable[position] = letter
        printtictactoetable(tictactoetable)
        if (checkDraw()):
            print("Draw!")
            exit()
        if checkForWin():
            if letter == 'X':
                print("Computer wins!")
                exit()
            else:
                print("Player wins!")
                exit()
        return
    else:
        print("Can't insert there! Position already occupied")
        position = int(input("Please enter different position:  "))
        insertLetter(letter, position)
        return
        
def checkForWin():
    if (tictactoetable[1] == tictactoetable[2] and tictactoetable[1] == tictactoetable[3] and tictactoetable[1] != ' '):
        return True
    elif (tictactoetable[4] == tictactoetable[5] and tictactoetable[4] == tictactoetable[6] and tictactoetable[4] != ' '):
        return True
    elif (tictactoetable[7] == tictactoetable[8] and tictactoetable[7] == tictactoetable[9] and tictactoetable[7] != ' '):
        return True
    elif (tictactoetable[1] == tictactoetable[4] and tictactoetable[1] == tictactoetable[7] and tictactoetable[1] != ' '):
        return True
    elif (tictactoetable[2] == tictactoetable[5] and tictactoetable[2] == tictactoetable[8] and tictactoetable[2] != ' '):
        return True
    elif (tictactoetable[3] == tictactoetable[6] and tictactoetable[3] == tictactoetable[9] and tictactoetable[3] != ' '):
        return True
    elif (tictactoetable[1] == tictactoetable[5] and tictactoetable[1] == tictactoetable[9] and tictactoetable[1] != ' '):
        return True
    elif (tictactoetable[7] == tictactoetable[5] and tictactoetable[7] == tictactoetable[3] and tictactoetable[7] != ' '):
        return True
    else:
        
        return False
        
def checkWhichMarkWon(mark):
    if tictactoetable[1] == tictactoetable[2] and tictactoetable[1] == tictactoetable[3] and tictactoetable[1] == mark:
        return True
    elif (tictactoetable[4] == tictactoetable[5] and tictactoetable[4] == tictactoetable[6] and tictactoetable[4] == mark):
        return True
    elif (tictactoetable[7] == tictactoetable[8] and tictactoetable[7] == tictactoetable[9] and tictactoetable[7] == mark):
        return True
    elif (tictactoetable[1] == tictactoetable[4] and tictactoetable[1] == tictactoetable[7] and tictactoetable[1] == mark):
        return True
    elif (tictactoetable[2] == tictactoetable[5] and tictactoetable[2] == tictactoetable[8] and tictactoetable[2] == mark):
        return True
    elif (tictactoetable[3] == tictactoetable[6] and tictactoetable[3] == tictactoetable[9] and tictactoetable[3] == mark):
        return True
    elif (tictactoetable[1] == tictactoetable[5] and tictactoetable[1] == tictactoetable[9] and tictactoetable[1] == mark):
        return True
    elif (tictactoetable[7] == tictactoetable[5] and tictactoetable[7] == tictactoetable[3] and tictactoetable[7] == mark):
        return True
    else:
        
        return False
        
def checkDraw():
    for key in tictactoetable.keys():
        if (tictactoetable[key] == ' '):
            return False
    
    return True
    
def playerMove():
    position = int(input("Enter the position for 'O':  "))
    insertLetter(player, position)

    return
    
def compMove():
    bestScore = -800
    bestMove = 0
    for key in tictactoetable.keys():
        if (tictactoetable[key] == ' '):
            tictactoetable[key] = bot
            score = minimax(tictactoetable, 0, False)
            tictactoetable[key] = ' '
            if (score > bestScore):
                bestScore = score
                bestMove = key
    insertLetter(bot, bestMove)
    
    return

def minimax(tictactoetable, depth, isMaximizing):
    if (checkWhichMarkWon(bot)):
        return 1
    elif (checkWhichMarkWon(player)):
        return -1
    elif (checkDraw()):
        return 0

    if (isMaximizing):
        bestScore = -800
        for key in tictactoetable.keys():
            if (tictactoetable[key] == ' '):
                tictactoetable[key] = bot
                score = minimax(tictactoetable, depth + 1, False)
                tictactoetable[key] = ' '
                if (score > bestScore):
                    bestScore = score
        return bestScore

    else:
        bestScore = 800
        for key in tictactoetable.keys():
            if (tictactoetable[key] == ' '):
                tictactoetable[key] = player
                score = minimax(tictactoetable, depth + 1, True)
                tictactoetable[key] = ' '
                if (score < bestScore):
                    bestScore = score
        return bestScore


tictactoetable = {1: ' ', 2: ' ', 3: ' ',
         4: ' ', 5: ' ', 6: ' ',
         7: ' ', 8: ' ', 9: ' '}

printtictactoetable(tictactoetable)
print("Computer goes first! Good luck.")
print("Positions are as follow:")
print("1, 2, 3 ")
print("4, 5, 6 ")
print("7, 8, 9 ")
print("\n")
player = 'O'
bot = 'X'

global firstComputerMove
firstComputerMove = True

while not checkForWin():
    compMove()
    playerMove()
