import random

field = [['-', '-', '-'],
         ['-', '-', '-'],
         ['-', '-', '-']]
         
def printField():
    ret = "\n"
    for i in range(3):
        for j in range(3):
            ret += f'{field[i][j]}    '
        ret += "\n"
    return ret

def personMove(msg):
    while True:
        pos = list(map(int,input(msg).strip().split(',')))
        x = pos[0]
        y = pos[1]
        if x >= 0 and x < 3 and y >= 0 and y < 3:
            if (field[x][y] == '-'):
                field[x][y] = 'X'
                break
            else:
                print(f'({x},{y}) invalid position!')
                continue

def computerMove():
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if field[x][y] == '-':
            field[x][y] = 'O'
            break

def run():
    print('tic tac toe')
    cont = 0
    while cont < 3:
        personMove('Make your move: ')
        computerMove()
        print(printField())
        cont+=1

run()