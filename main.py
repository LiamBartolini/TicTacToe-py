import random

print('tic tac toe')
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

def pearsoneMove():
    pos = list(map(int,input('Input your position (x,y) - ').strip().split(',')))
    x = pos[0]
    y = pos[1]
    if x >= 0 and x < 3 and y >= 0 and y < 3:
        if (field[x][y] == '-'):
            field[x][y] = 'X'
        else:
            print(f'({x},{y}) invalid position!')

def computerMove():
    while True:
        x = random.randint(0,2)
        y = random.randint(0,2)
        if field[x][y] == '-':
            field[x][y] = 'O'
            break

computerMove()
print(printField())