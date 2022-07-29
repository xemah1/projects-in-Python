from random import randint


w = randint(5,9)
gameOn = 1
grid = [[0 for i in range(w)]for i in range(w)]
fakeGrid = [["█" for i in range(w)]for i in range(w)]
mineCount = randint(w//2,w*w//5)
moveJ = [-1,-1,0,1,1,1,0,-1]
moveI = [0,1,1,1,0,-1,-1,-1]

# placing mines
for i in range(mineCount) :
    grid[randint(0,w-1)][randint(0,w-1)] = "M"

# determining how many mines are adjacent to that tile
for i in range(w) :
    for j in range(w) :
        counter = 0
        if (grid[j][i] == 0) :
            for k in range(len(moveI)) :
                if (i + moveI[k] < w and i + moveI[k] >= 0 and j + moveJ[k] < w and j + moveJ[k] >= 0) :
                    if (grid[j + moveJ[k]][i + moveI[k]] == "M") :
                        counter += 1
            grid[j][i] = counter

def printGrid(fakeGrid, w) :
    print("  ",end="")
    for i in range(w) :
        print("  " + str(i+1) + " " , end="")
    print()
    print("  ┌", end="")
    for i in range((w*3)+w-1) :
        print("─", end="")
    print("┐")
    for i in range(w) :
        print(str(i+1) + " ",end="")
        for k in range(w) :
            print("│ " + str(fakeGrid[k][i]), end=" ")
        print("│")
        if (i != w-1) :
            print("  │", end="")
            for k in range((w*3)+w-1) :
                print("─", end="")
            print("│")
        elif (i == w-1) :
            print("", end="")
            print("  └", end="")
            for i in range((w*3)+w-1) :
                print("─", end="")
            print("┘")

# checks your choices
def isRevealed(grid, fakeGrid, choice, moveJ, moveI, w, gameOn) :
    x,y = int(choice.split(None, 1)[0]) - 1, int(choice.split(None, 1)[1]) - 1
    """
    if (grid[x][y] == 0) :
        fakeGrid[x][y] = " "
        for k in range(len(moveI)) :
            if (y + moveI[k] < 5 and y + moveI[k] >= 0 and x + moveJ[k] < 5 and x + moveJ[k] >= 0) :
                choice = str(x + moveJ[k]) + " " + str(y + moveI[k])
                if (grid [int(choice.split(None, 2)[0])][int(choice.split(None, 2)[1])] == 0) :
                    fakeGrid [int(choice.split(None, 2)[0])][int(choice.split(None, 2)[1])] == " "
                isRevealed(grid, fakeGrid, choice, moveJ, moveI, w, gameOn)
        gameOn = 0
        return gameOn
    """
    for i in range(w) :
        for k in range(w) :
            if (grid[k][i] == 0) :
                fakeGrid[i][k] = " "

    if (grid[x][y] == "M") :
        fakeGrid[x][y] == "M"
        gameOn = 0
        return gameOn
    else :
        fakeGrid[x][y] = grid[x][y]
        gameOn = 1
        return gameOn

def isWin(grid, fakeGrid, w) :
    for i in range(w) :
        for k in range(w) :
            if (grid[k][i] != "M" and fakeGrid[k][i] == "█") :
                return False
    return True


printGrid(fakeGrid, w)
print("Example input: " + str(randint(1,w)) + " " + str(randint(1,w)))
while gameOn == 1 :
    choice = input("Input: ")
    gameOn = isRevealed(grid, fakeGrid, choice, moveJ, moveI, w, gameOn)
    printGrid(fakeGrid, w)
    if (gameOn == 0) :
        print("Game Over. Mine found.")
        printGrid(grid, w)
    if (isWin(grid, fakeGrid, w)) :
        print("You won.")
        printGrid(grid, w)
        gameOn = 0