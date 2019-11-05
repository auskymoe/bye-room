import random
import pprint
from math import floor

lr = .4
ep = .2
gam = .4
qs = [[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]],[[0,0,0],[0,0,0],[0,0,0],[0,0,0]]
done = False
mov = []

def make_q(qs):
    for i in range(25): #state
        for j in range(4): #action
            qs[i][j] = [0,-1,False]        #qvalue, reward, acheived
    
def move(x):
    if x < 1:
        return [1,0]
    if x < 2:
        return [-1,0]
    if x < 3:
        return [0,1]
    return [0,-1]

def maxi(directs):
    m = directs[0][1]
    for i in range(len(directs)):
        if directs[i][1] > m:
            m = directs[i][1]
    return m

def maxq(directs):
    if directs[1][0] == directs[2][0] and directs[3][0] == directs[0][0] and directs[0][0] == directs[2][0]:
            return floor(random.uniform(0,1) * 4)
    j = 0;
    m = directs[0][0]
    for i in range(len(directs)):
        if directs[i][0] > m:
            m = directs[i][0]
            j = i
        
    return j
rl = 0
rd = 0
make_q(qs)
eps = 50
while eps > 0:
    print("STARTARTAROITAROTIHAROITHAORITHOARIHTOAIRHT")
    px = 0
    py = 2
    tx = 4
    ty = 3
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    board[tx][ty] = 1
    board[px][py] = 'P'
    eps -= 1
    done = False
    while not done:
        if random.uniform(0,1) < ep:
            direction = int(floor(random.uniform(0,1) * 4))
            print(direction)
            mov = move(random.uniform(0,1) * 4)
            while (px + mov[0] >= 5 or px + mov[0] < 0 or py + mov[1] >= 5 or py + mov[1] < 0):
                mov = move(random.uniform(0,1) * 4)
            if (board[px+mov[0]][py+mov[1]] == 1):
                reward = 20
            else:
                reward = qs[px * 5 + py][direction][1]
            qs[px * 5 + py][direction][0] = qs[px * 5 + py][direction][0]*(1-lr) + lr * (reward + gam * maxi(qs[(px + mov[0]) * 5 + py + mov[1]]))
        else:
            direction = maxq(qs[px * 5 + py])
            print(direction)
            mov = move(direction)
            while (px + mov[0] >= 5 or px + mov[0] < 0 or py + mov[1] >= 5 or py + mov[1] < 0):
                mov = move(random.uniform(0,1) * 4)
            if (board[px+mov[0]][py+mov[1]] == 1):
                reward = 20
            else:
                reward = qs[px * 5 + py][direction][1]
            qs[px * 5 + py][direction][0] = qs[px * 5 + py][direction][0]*(1-lr) + lr * (reward + gam * maxi(qs[(px + mov[0]) * 5 + py + mov[1]]))
        board[px][py] = 0;
        px += mov[0]
        py += mov[1]
        done = board[px][py] == 1
        board[px][py] = 'P'
        pprint.pprint(board)
        print()
        rl += 1
eps = 50
while eps > 0:
    print("STARTARTAROITAROTIHAROITHAORITHOARIHTOAIRHT")
    px = 0
    py = 2
    tx = 4
    ty = 3
    board = [[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0],[0,0,0,0,0]]
    board[tx][ty] = 1
    board[px][py] = 'P'
    eps -= 1
    done = False
    while not done:
        direction = int(floor(random.uniform(0,1) * 4))
        print(direction)
        mov = move(random.uniform(0,1) * 4)
        while (px + mov[0] >= 5 or px + mov[0] < 0 or py + mov[1] >= 5 or py + mov[1] < 0):
            mov = move(random.uniform(0,1) * 4)
        if (board[px+mov[0]][py+mov[1]] == 1):
            reward = 20
        else:
            reward = qs[px * 5 + py][direction][1]
        qs[px * 5 + py][direction][0] = qs[px * 5 + py][direction][0] + lr * (reward + gam * maxi(qs[(px + mov[0]) * 5 + py + mov[1]]) - qs[px * 5 + py][direction][0])
        board[px][py] = 0;
        px += mov[0]
        py += mov[1]
        done = board[px][py] == 1
        board[px][py] = 'P'
        pprint.pprint(board)
        print()
        rd += 1
print(rl,rd)
        
        
            
            
            
    
