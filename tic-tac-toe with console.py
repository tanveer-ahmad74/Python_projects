board = {1:' ', 2:' ', 3:' ',
         4:' ', 5:' ', 6:' ',
         7:' ', 8:' ', 9:' '}


def PrintBoard(board):
    print('------------------')
    print(' ', board[1]+ ' | ' + board[2] + ' | ', board[3])
    print('-----------------')
    print(' ', board[4]+ ' | ', board[5] + ' | ', board[6])
    print('-----------------')
    print(' ', board[7]+ ' | ', board[8] + ' | ', board[9])
    print('-----------------')

PrintBoard(board)

def isSpacefree(position):
    if (board[position])  == ' ':       #empty
        return True
    else:
        return False

def CheckforDraw():
    for key in board.keys():
        if board[key] == ' ':
            return False

    return True

def CheckForWin():
    if (board[1] == board[2] and board[1] == board[3] and board[1] != ' '):
        return True
    elif (board[4] == board[5] and board[4] == board[6] and board[4] != ' '):
        return True
    elif (board[7] == board[8] and board[7] == board[9] and board[7] != ' '):
        return True
    elif (board[1] == board[4] and board[1] == board[7] and board[1] != ' '):
        return True
    elif (board[2] == board[5] and board[2] == board[8] and board[2] != ' '):
        return True
    elif (board[3] == board[6] and board[3] == board[9] and board[3] != ' '):
        return True
    elif (board[1] == board[5] and board[1] == board[9] and board[1] != ' '):
        return True
    elif (board[7] == board[5] and board[7] == board[3] and board[7] != ' '):
        return True
    else:
        return False

def insertLetter(letter,position):
    if isSpacefree(position):
        board[position] = letter
        PrintBoard(board)
        if(CheckforDraw()):
            print("Draw")
            exit()

        if(CheckForWin()):
            if letter == 'X':
                print("Computre wins...!")
                exit()
            else:
                print("Player Wins")
                exit()
        return
    else:
        print("Can not insert there..!")
        position = int(input("Enter new position..!"))
        insertLetter(letter,position)
        return
Computer = 'X'
player = 'O'
def PlayerMove():
    position = int(input("ENter the position for PlayerMove: "))
    insertLetter(player,position)
    return
def ComputerMove():
    position = int(input("ENter the position for ComputerMove:"))
    insertLetter(Computer,position)
    return
while not CheckForWin():
    ComputerMove()
    PlayerMove()



