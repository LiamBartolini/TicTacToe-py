import random
board = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
         
def printField():
    ret = "\n"
    for i in range(3):
        for j in range(3):
            ret += f'{board[i][j]}    '
        ret += "\n"
    return ret

def personMove(msg):
    while True:
        pos = list(map(int,input(msg).strip().split(',')))
        x = pos[0]
        y = pos[1]
        if x >= 0 and x < 3 and y >= 0 and y < 3:
            if (board[x][y] == '-'):
                board[x][y] = 'X'
                break
            else:
                print(f'({x},{y}) invalid position!')
                continue

def computerMove():
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if board[x][y] == '-':
            board[x][y] = 'O'
            break

def run():
    print('tic tac toe')
    cont = 0
    while True:
        personMove('Make your move: ')
        computerMove()
        print(printField())
        cont+=2
        if cont >= 5:
            if win('X'): # verify if there is a winner
                break
            if win('O'): # verify if there is a winner
                break

def win(symbol):
    if board[0][0] == symbol and board[1][1] == symbol and board[2][2] == symbol: # main diagonal
        print(f'The Winner is \'{symbol}\' ')
        return True
    
    if board[0][2] == symbol and board[1][1] == symbol and board[2][0] == symbol: # second diagonal
        print(f'The Winner is \'{symbol}\' ')
        return True
    
    if board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol: # first column
        print(f'The Winner is \'{symbol}\' ')
        return True
    
    if board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol: # second column
        print(f'The Winner is \'{symbol}\' ')
        return True
    
    if board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol: # third column
        print(f'The Winner is \'{symbol}\' ')
        return True
    
    #(riga, colonna)
    if board[0][0] == symbol and board[1][0] == symbol and board[2][0] == symbol: # first row
        print(f'The Winner is \'{symbol}\' ')
        return True
        
    if board[1][0] == symbol and board[1][1] == symbol and board[1][2] == symbol: # second row
        print(f'The Winner is \'{symbol}\' ')
        return True
    
    if board[2][0] == symbol and board[2][1] == symbol and board[2][2] == symbol: # third row
        print(f'The Winner is \'{symbol}\' ')
        return True

run()