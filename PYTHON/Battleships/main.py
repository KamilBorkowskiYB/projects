#             2x,3x,4x,5x
sunken_ships = [0,0,0,0]


def show(x):
   for i in x:
       print(i)


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
                pos_3x[k][l] =pos_3x[k][l]*2
    if sunken_ships[1] == 1:
        calculate_matrices(3)
    if sunken_ships[2] == 0:
        calculate_matrices(4)
    if sunken_ships[3] == 0:
        calculate_matrices(5)

    for i in range(10):
        for j in range(10):
            sum_pos[i][j] = pos_2x[i][j]+pos_3x[i][j]+pos_4x[i][j]+pos_5x[i][j]


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
    pass


def hit_or_miss():
    pass


def ship_sunken():
    pass


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

pos_3x_2 = [
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
    [0,0,0,0,0,1,0,0,0,0],
    [0,0,0,0,1,0,1,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,0],
    [0,0,0,0,0,0,0,0,0,1],
    [0,0,0,0,0,0,0,0,1,0],
    [0,0,0,0,0,0,0,0,1,0],
    ]

seek_target()
show(sum_pos)
