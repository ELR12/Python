# Created by
# Ethan Roberts
# on 03/28/2020
#
# This is my first Python program where I implement a Sudoku puzzle.  This program was created
# for CS472, Analysis of Algorithm.


# cite: https://medium.com/generative-design/fundamentals-of-python-variables-b0523dd698a7
# cite: https://stackoverflow.com/questions/4706499/how-do-you-append-to-a-file-in-python
# cite: https://stackoverflow.com/questions/16739555/python-if-not-syntax
# cite:  https://www.youtube.com/watch?v=QI0diwmx3OY
# cite: https://docs.python.org/3/
# cite: https://docs.python.org/3/tutorial/datastructures.html#list-comprehensions  (for init-ing 2-D array variable)


def printBoardToTerminal(board):
    print("---------------------")
    for x in range(0, 9):
        if x == 3 or x == 6:
            print("---------------------")
        for y in range(0, 9):
            if y == 3 or y == 6:
                print("|", end=" ")
            print(board[x][y], end=" ")
        print()
    print("---------------------")
    print()
    print()






def printBoardToFile(board):
    file = open("outfile.txt", "a")
    file.write("-------------------\n")
    for x in range(0, 9):
        if x == 3 or x == 6:
            file.write("-------------------\n")
        for y in range(0, 9):
            if y == 3 or y == 6:
                file.write("|")
            file.write(str(board[x][y]) + " ")
        file.write("\n")
    file.write("-------------------\n\n\n\n")
    file.close()






def createBoard(board):  #function that reads file and creates sudoku board
    filepath = "testInputData.txt"
    with open(filepath) as fp:
        for x in range(0,9):
            for y in range (0,9):
                line = fp.readline()
                board[x][y] = int(line.strip(),10) #strips newline from read-in char, and then type-casts char to int






def isFullBoard(board):
    for x in range(0,9):
        for y in range(0,9):
            if board[x][y] == 0:
                return False
    return True






# passing in the sudoku board, and the "i,j" param which is the coords of the empty cell found
def getUsableSymbols(board, i, j):
    cellDictionary = {}
    r = 0
    c = 0

    for x in range(1,10):
        cellDictionary[x] = 0

    for x in range(0,9): #checks entire row
        if board[i][x] != 0:  # if  not zero, then cell has a symbol already
            cellDictionary[board[i][x]] = 1      # marking with 1 to symbolize cell is taken

    for x in range(0,9): #checks entire column
        if not board[x][j] == 0:  # if  not zero, then cell has a symbol already
            cellDictionary[board[x][j]] = 1      # marking with 1 to symbolize cell is taken


    # Get what "rank" you're in (rank is a sudoku term that refers to
    # the three major horizontal rows of a sudoku puzzle.)
    if i >= 0 and i <= 2:      #in rank one
        r = 0
    elif i >= 3 and i <=5:     #in rank two
        r = 3
    else:                      #in rank three
        r = 6

    # Get what "stack" you're in (stack is a sudoku term that refers to
    # the three major vertical columns of a sudoku puzzle.)
    if j >= 0 and j <= 2:      #in stack one
        c = 0
    elif j >= 3 and j <=5:     #in stack two
        c = 3
    else:                      #in stack three
        c = 6


    # Now search the dictionary and store a symbol that has not been used yet
    # (loop range of 1-9 since these are sudoku values for the puzzle)
    for x in range(1,10):
        if cellDictionary[x] == 0:
            cellDictionary[x] = x  # fill empty space with a symbol that is available to use
        else:
            cellDictionary[x] = 0  # marking used ones as zero

    return cellDictionary




def solveSudokuPuzzle(board):
    i = 0
    j = 0
    usableSymbols = {}

    if isFullBoard(board):
        print ("Sudoku Puzzle has been successfully solved!")
        printBoardToTerminal(board)
        printBoardToFile(board)
        exit()
        return
    else:
        for x in range(0,9):
            for y in range(0,9):
                if board[x][y] == 0:   # empty cell found
                    i = x
                    j = y

        # gets all possible symbols that can be used for this empty cell
        usableSymbols = getUsableSymbols(board, i, j)

        for x in range(1, 10):
            if usableSymbols[x] != 0:
                board[i][j] = usableSymbols[x]
                solveSudokuPuzzle(board)

        # if you get to this point, then there were so
        # possible symbols to use on your previous move, therefore you made a bad move and need
        # to erase your past move
        board[i][j] = 0






def main():
    sudokuBoard = [[0 for x in range(9)] for x in range(9)] # creates 2-D array
    createBoard(sudokuBoard)
    printBoardToTerminal(sudokuBoard)
    printBoardToFile(sudokuBoard)
    solveSudokuPuzzle(sudokuBoard)
    printBoardToTerminal(sudokuBoard)


if __name__ == "__main__":
    main()
