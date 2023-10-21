import random
#             2x,3x,4x,5x
sunken_ships = [0,0,0,0]
ship_hit = False

def show(x):
   for i in x:
       print(i)


def move():
    global ship_hit
    seek_target()
    show(sum_pos)
    where_to_shot()
    show(hits)
    clear_pos()


# calculates sum of possibilities of ships
def seek_target():
    global sunken_ships
    global pos_2x
    global pos_3x
    global pos_4x
    global pos_5x
    global sum_pos
    if sunken_ships[0] == 0:
        calculate_matrices(2)
    if sunken_ships[1] == 0:
        calculate_matrices(3)
        for k in range(10):
            for l in range(10):
                pos_3x[k][l] = pos_3x[k][l]*2
    if sunken_ships[1] == 1:
        calculate_matrices(3)
    if sunken_ships[2] == 0:
        calculate_matrices(4)
    if sunken_ships[3] == 0:
        calculate_matrices(5)

    for i in range(10):
        for j in range(10):
            sum_pos[i][j] = pos_2x[i][j]+pos_3x[i][j]+pos_4x[i][j]+pos_5x[i][j]

    target_hit()


# calculates possibilities of individual ships
def calculate_matrices(length):
    global pos_2x
    global pos_3x
    global pos_4x
    global pos_5x
    global hits
    if length == 2:
        for i in range(10):
            for j in range(10-length+1):
                if hits[i][j] == 0 and hits[i][j+1] == 0:
                    pos_2x[i][j] += 1
                    pos_2x[i][j+1] += 1
        for k in range(10-length+1):
            for l in range(10):
                if hits[k][l] == 0 and hits[k+1][l] == 0:
                    pos_2x[k][l] += 1
                    pos_2x[k+1][l] += 1
    elif length == 3:
        for i in range(10):
            for j in range(10 - length + 1):
                if hits[i][j] == 0 and hits[i][j + 1] == 0 and hits[i][j + 2] == 0:
                    pos_3x[i][j] += 1
                    pos_3x[i][j + 1] += 1
                    pos_3x[i][j + 2] += 1
        for k in range(10 - length + 1):
            for l in range(10):
                if hits[k][l] == 0 and hits[k + 1][l] == 0 and hits[k + 2][l] == 0:
                    pos_3x[k][l] += 1
                    pos_3x[k + 1][l] += 1
                    pos_3x[k + 2][l] += 1
    elif length == 4:
        for i in range(10):
            for j in range(10 - length + 1):
                if hits[i][j] == 0 and hits[i][j + 1] == 0 and hits[i][j + 2] == 0 and hits[i][j + 3] == 0:
                    pos_4x[i][j] += 1
                    pos_4x[i][j + 1] += 1
                    pos_4x[i][j + 2] += 1
                    pos_4x[i][j + 3] += 1
        for k in range(10 - length + 1):
            for l in range(10):
                if hits[k][l] == 0 and hits[k + 1][l] == 0 and hits[k + 2][l] == 0 and hits[k + 3][l] == 0:
                    pos_4x[k][l] += 1
                    pos_4x[k + 1][l] += 1
                    pos_4x[k + 2][l] += 1
                    pos_4x[k + 3][l] += 1
    elif length == 5:
        for i in range(10):
            for j in range(10 - length + 1):
                if hits[i][j] == 0 and hits[i][j + 1] == 0 and hits[i][j + 2] == 0 and hits[i][j + 3] == 0 and hits[i][j + 4] == 0:
                    pos_5x[i][j] += 1
                    pos_5x[i][j + 1] += 1
                    pos_5x[i][j + 2] += 1
                    pos_5x[i][j + 3] += 1
                    pos_5x[i][j + 4] += 1
        for k in range(10 - length + 1):
            for l in range(10):
                if hits[k][l] == 0 and hits[k + 1][l] == 0 and hits[k + 2][l] == 0 and hits[k + 3][l] == 0 and hits[k + 4][l] == 0:
                    pos_5x[k][l] += 1
                    pos_5x[k + 1][l] += 1
                    pos_5x[k + 2][l] += 1
                    pos_5x[k + 3][l] += 1
                    pos_5x[k + 4][l] += 1


def target_hit():
    global sum_pos
    global hits
    global ship_hit
    for i in range(10):
        for j in range(10):
            if hits[i][j] == 2:
                if hits[i+1][j] == 2 or hits[i-1][j] == 2:
                    if sum_pos[i-1][j] != 0:
                        sum_pos[i-1][j] += 50
                    if sum_pos[i+1][j] != 0:
                        sum_pos[i+1][j] += 50
                elif hits[i][j+1] == 2 or hits[i][j-1] == 2:
                    if sum_pos[i][j+1] != 0:
                        sum_pos[i][j+1] += 50
                    if sum_pos[i][j-1] != 0:
                        sum_pos[i][j-1] += 50
                else:
                    if sum_pos[i-1][j] != 0:
                        sum_pos[i-1][j] += 50
                    if sum_pos[i][j-1] != 0:
                        sum_pos[i][j-1] += 50
                    if sum_pos[i+1][j] != 0:
                        sum_pos[i+1][j] += 50
                    if sum_pos[i][j+1] != 0:
                        sum_pos[i][j+1] += 50


def where_to_shot():
    global sum_pos
    global hits
    global ship_hit
    num_of_high_tiles = 0
    maks = 0
    for i in range(10):
        for j in range(10):
            if sum_pos[i][j] >= maks:
                x = i
                y = j
                maks = sum_pos[i][j]
    for k in range(10):
        for l in range(10):
            if sum_pos[k][l] == maks:
                num_of_high_tiles += 1
    if num_of_high_tiles > 1:
        x = random.randrange(10)
        y = random.randrange(10)
        while sum_pos[x][y] != maks:
            x = random.randrange(10)
            y = random.randrange(10)

    print(x)
    print(y)
    print(maks)
    print(num_of_high_tiles)
    #print(hit_or_miss(x,y))
    if hit_or_miss(x,y):
        hits[x][y] = 2
        ship_hit = True
    else:
        hits[x][y] = 1
        ship_hit = False


def hit_or_miss(i, j):
    global ships
    if ships[i][j] == 'X':
        return True
    else: return  False


def update_hits():
    pass


def ship_sunken():
    pass


def clear_pos():
    global pos_2x
    global pos_3x
    global pos_4x
    global pos_5x
    for i in range(10):
        for j in range(10):
            pos_2x[i][j] = 0
            pos_3x[i][j] = 0
            pos_4x[i][j] = 0
            pos_5x[i][j] = 0


ships = [
    [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [ 0 , 0 ,'X','X', 0 , 0 , 0 , 0 , 0 , 0],
    [ 0 , 0 , 0 , 0 , 0 , 0 ,'X', 0 , 0 ,'X'],
    [ 0 , 0 , 0 , 0 , 0 , 0 ,'X', 0 , 0 ,'X'],
    [ 0 ,'X', 0 , 0 , 0 , 0 ,'X', 0 , 0 ,'X'],
    [ 0 ,'X', 0 , 0 , 0 , 0 ,'X', 0 , 0 , 0],
    [ 0 ,'X', 0 , 0 , 0 , 0 ,'X', 0 , 0 , 0],
    [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    [ 0 , 0 , 0 ,'X','X','X','X', 0 , 0 , 0],
    [ 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0 , 0],
    ]

pos_2x = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]

pos_3x = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]

pos_4x = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]

pos_5x = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]

sum_pos = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]

hits = [
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    ]

move()
print('--------------------')
move()
print('--------------------')
move()
print('--------------------')
move()
print('--------------------')
move()
print('--------------------')
move()
print('--------------------')
move()
print('--------------------')
move()

