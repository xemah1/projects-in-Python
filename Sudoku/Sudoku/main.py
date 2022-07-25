from random import sample
import os

def play() :
    base  = 3
    side  = base*base

    print("═══════════════════════════════════════════════════════════════════════════════════════════════════════════════════")
    def createBoard() :


        # pattern for a baseline valid solution
        def pattern(r,c): return (base*(r%base)+r//base+c)%side

        # randomize rows, columns and numbers (of valid base pattern)
        def shuffle(s): return sample(s,len(s)) 
        rBase = range(base) 
        rows  = [ g*base + r for g in shuffle(rBase) for r in shuffle(rBase) ] 
        cols  = [ g*base + c for g in shuffle(rBase) for c in shuffle(rBase) ]
        nums  = shuffle(range(1,base*base+1))

        # produce board using randomized baseline pattern
        board = [ [nums[pattern(r,c)] for c in rows] for r in cols ]
        boardKeep = [ [0 for k in range(side)] for i in range(side) ]

        for k in range(side) :
            for i in range(side) :
                boardKeep[i][k] = board[i][k]
        
        # empties the board so player can fill it 
        # x//81 removes x amount of numbers from the board
        squares = side*side
        empties = squares * 17//81
        for p in sample(range(squares),empties):
            board[p//side][p%side] = 0

        return board,boardKeep,base,side

    board,boardKeep,base,side = createBoard()


    def clearConsole() :
        if(os.name == "prolix") :
            os.system("clear")
        else :
            os.system("cls")


    def printBoard(board) :


        # clearConsole() # remove the first comment symbol on this line if you are running this on command prompt


        def expandLine(line):
            return line[0]+line[5:9].join([line[1:5]*(base-1)]*base)+line[9:13]
        line0  = expandLine("╔═══╤═══╦═══╗")
        line1  = expandLine("║ . │ . ║ . ║")
        line2  = expandLine("╟───┼───╫───╢")
        line3  = expandLine("╠═══╪═══╬═══╣")
        line4  = expandLine("╚═══╧═══╩═══╝")

        symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
        nums   = [ [""]+[symbol[n] for n in row] for row in board ]
        print(line0)
        for r in range(1,side+1):
            print( "".join(n+s for n,s in zip(nums[r-1],line1.split("."))) )
            print([line2,line3,line4][(r%side==0)+(r%base==0)])

    printBoard(board)
    counter = 0

    # loop to play the game
    while True :
        a = ""
        counter = 0
        print()
        choice = input("Example Input (Row ; Column ; Input): 3 7 2 \\\ ")
        choiceArr = [ (int(choice.split(None, 2)[0]))-1,
                    (int(choice.split(None, 2)[1]))-1,
                    (int(choice.split(None, 2)[2])) ]

        if( board [choiceArr [0]][choiceArr [1]] == 0) :
            board [choiceArr [0]][choiceArr [1]] = choiceArr [2]
            printBoard(board)
        else :
            print("Wrong Input.")
        for k in range(side) :
            for i in range(side) :
                if(board [i][k] != 0) :
                    counter += 1
        if(counter == side*side) :
            print("Board completed.")
            if(board == boardKeep) :
                print("Sudoku completed successfully. Congratulations.\nWould you like to try again? [New / Quit]")
                a = input()
                a = a.upper()
                if (a == "NEW") :
                    return 0
                elif (a == "QUIT") :
                    return 2
            else :
                
                print("Correct solution was:")
                for line in boardKeep : print(line)
                print()

                print("Mistakes were made and Sudoku was not completed successfully.\nWould you like to try again? [New / Quit]")
                a = input()
                a = a.upper()

        if (a == "NEW"):
            return 0
        elif (a == "QUIT") :
            return 2


# loop to start the game
b = 0
c = 0
while b == 0 :
    if (c == 0) :
        c = play()
    else :
        print("Thank you for playing.")
        break