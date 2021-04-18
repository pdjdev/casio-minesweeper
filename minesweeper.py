# casio-minesweeper
# A simple minesweeper python script for CASIO calculator (9860G3)
# by @pdjdev (https://github.com/pdjdev/)

import random

width = 21
height = 5

playing = True

# Printing Main Title
def print_title():
    print('+-------------------+')
    print('| MINE SWEEPER      |')
    print('|       by @PDJDEV  |')
    print('+-------------------+')

# Printing Raw Map
def print_raw_map(mapdata):
    for i in mapdata:
        for j in i:
            if (j == 0):
                print('.', end='')
            elif (j == -1):
                print('*', end='')
            else:
                print(str(j), end='')
        print()

# Printing Normal Map
def print_map(mapdata, clickdata):
    for y in range(height):
        for x in range(width):
            if (clickdata[y][x] == 0):
                print('L', end = '')
            elif (clickdata[y][x] == -1):
                print('#', end = '')
            else:
                if (mapdata[y][x] == -1):
                    print('*', end = '')
                elif (mapdata[y][x] == 0):
                    print('.', end = '')
                else:
                    print(str(mapdata[y][x]), end = '')
        print()


# Adding numbers to the cell
def addnum(mapdata, y, x):
    if (y >= 0 and y < height and x >= 0 and x < width):
        if (mapdata[y][x] != -1):
            mapdata[y][x] += 1


# For Auto-click
def singleclick(clickdata, y, x):
    if (y >= 0 and y < height and x >= 0 and x < width):
        if (clickdata[y][x] == 1): return False
        clickdata[y][x] = 1
        return True    


# Click x, y cell & auto-click empty cells
def click(mapdata, clickdata, y, x):
    if flag:
        if (clickdata[y][x] == -1):
            clickdata[y][x] = 0
        else:
            clickdata[y][x] = -1
        return True
    
    if (mapdata[y][x] == -1):
        return False

    else:
        if (clickdata[y][x] == 1):
            pass

        elif (clickdata[y][x] == 0):
            clickdata[y][x] = 1

            if (mapdata[y][x] == 0):
                delta = True
                
                while(delta):
                    delta = False
                    for y2 in range(height):
                        for x2 in range(width):
                            if (clickdata[y2][x2] == 1 and mapdata[y2][x2] == 0):
                                if singleclick(clickdata, y2-1, x2-1): delta = True
                                if singleclick(clickdata, y2-1, x2): delta = True
                                if singleclick(clickdata, y2-1, x2+1): delta = True
                                if singleclick(clickdata, y2, x2-1): delta = True
                                if singleclick(clickdata, y2, x2+1): delta = True
                                if singleclick(clickdata, y2+1, x2-1): delta = True
                                if singleclick(clickdata, y2+1, x2): delta = True
                                if singleclick(clickdata, y2+1, x2+1): delta = True
                                
        return True


# Check whether a game is cleared or not
def clear_check(mapdata, clickdata):
    for y in range(height):
        for x in range(width):
            if (mapdata[y][x] != -1):
                if (clickdata[y][x] != 1):
                    return False
    return True

# Check number of flags
def flag_check(clickdata):
    flags = 0
    for y in range(height):
        for x in range(width):
            if (clickdata[y][x] == -1):
                flags += 1
    return flags



# MAIN LOOP
while (playing):

    print_title()
    
    mmap = []
    cmap = []
    cx = ''
    cy = ''
    flag = False

    print('Number of mines?(~99)\n')

    errorlv = True

    while (errorlv):
        try:
            mines = int(input('> '))
            if (mines < 1 or mines > 99):
                print_title()
                print('    Please enter\n   between 1 to 99')
                errorlv = True
                continue
            errorlv = False
        except:
            print_title()
            print('    Please enter\n     valid value  ')
            errorlv = True

    # Initiating Map
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        mmap.append(row)

    # Initiating Clicked Map
    for i in range(height):
        row = []
        for j in range(width):
            row.append(0)
        cmap.append(row)

    # Placing Mines
    for i in range(mines):
        x = random.randrange(0, width)
        y = random.randrange(0, height)

        while (mmap[y][x] == -1):
            x = random.randrange(0, width)
            y = random.randrange(0, height)
            
        mmap[y][x] = -1

    # Adding Numbers
    for y in range(height):
        for x in range(width):
            if (mmap[y][x] == -1):
                addnum(mmap, y-1, x-1)
                addnum(mmap, y-1, x)
                addnum(mmap, y-1, x+1)
                addnum(mmap, y, x-1)
                addnum(mmap, y, x+1)
                addnum(mmap, y+1, x-1)
                addnum(mmap, y+1, x)
                addnum(mmap, y+1, x+1)

    errorlv = False

    while (True):
        if not errorlv: print('[W:' + str(width) + ' H:'+str(height) + ' MINE: ' + str(mines-flag_check(cmap)) + ']====')
        print_map(mmap, cmap)

        if (cx == '' or cy == ''):
            print('Enter (x.y)', end='')
        else: 
            print('Prev:'+cx+'.'+cy, end='')

        if flag:
            print(' Flag', end='')

        inp = input(' > ')

        if '+' in inp:
            flag = not flag
            errorlv = True
            if flag: print('[Flag mode ON]=======')
            else: print('[Flag mode OFF]======')
            continue

        try:
            if (inp == ''):
                print('[Enter x.y location]=')
                errorlv = True
                continue
            
            cx, cy = inp.split('.')

            if (int(cx) > width or int(cy) > height):
                print('[Out of range!]======')
                errorlv = True
                continue

            if (not click(mmap, cmap, int(cy)-1, int(cx)-1)):
                print('[GAME OVER]==========')
                print_raw_map(mmap)
                if (input('Replay? (Yes=+)> ') != '+'):
                    playing = False
                break

            if (clear_check(mmap, cmap)):
                print('[GAME CLEAR]=========')
                print_raw_map(mmap)
                if (input('Replay? (Yes=+)> ') != '+'):
                    playing = False
                break
            
        except:
            print('[Try Again]==========')
            errorlv = True
            continue

        errorlv = False
