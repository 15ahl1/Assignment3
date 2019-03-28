
def readInput(path):
    output = []
    with open(path, "r") as file:
        generation = file.readline()
        lines = file.read().splitlines()
        for i in lines:
            temp = []
            for item in i:
                temp.append(int(item))
            output.append(temp)
    file.close()
    return output, generation

#Writes board and generation to file
def addToFile(path, board, gen):
    with open(path, "a") as file:
        file.write("Generation " + str(gen) + "\n")
        for row in board:
            temp = ""
            for elem in row:
                temp += (str(elem) + "")
            file.write(temp + "\n")
    file.close()

#Formats and prints the board
def printBoard(board):
    for row in board:
        for elem in row:
            print(elem),
        print("\n")
    print("\n")


#Calculates the number of live neighbours per square
def calculateLiveNeighbours(board, x, y):
    count = 0
    xLen = len(board)
    yLen = len(board[0])

    #Up
    if y - 1 >= 0 and board[x][y - 1] == 1:
        count += 1
    #Down
    if y + 1 < yLen and board[x][y + 1] == 1:
        count += 1
    #Left
    if x - 1 >= 0 and board[x - 1][y] == 1:
        count += 1
    #Right
    if x + 1 < xLen and board[x + 1][y] == 1:
        count += 1
    #TopLeft
    if x - 1 >= 0 and y - 1 >= 0 and board[x - 1][y - 1] == 1:
        count += 1
    #TopRight
    if x + 1 < xLen and y - 1 >= 0 and board[x + 1][y - 1] == 1:
        count += 1
    #BottomLeft
    if x - 1 >= 0 and y + 1 < yLen and board[x - 1][y + 1] == 1:
        count += 1
    #BottomRight
    if x + 1 < xLen and y + 1 < yLen and board[x + 1][y + 1] == 1:
        count += 1
    #print("Position (" + str(x) + ", " + str(y) + ") = " + str(count))
    return count


# Returns a table containing the number
# of live neighbours for each square
def onOffTable(board):
    xLen = len(board[0])
    yLen = len(board)
    output = []
    for row in range(yLen):
        temp = []
        for elem in range(xLen):
            temp.append(calculateLiveNeighbours(board, row, elem))
        output.append(temp)
    return output

#Returns the next generation of the current board
def getNextGeneration(board):
    liveTable = onOffTable(board)
    output = []
    for i in range(len(board)):
        temp = []
        for j in range(len(board[0])):
            if(board[i][j] == 1 and liveTable[i][j] in range(2, 4)):
                temp.append(1)
            elif(liveTable[i][j] == 3):
                temp.append(1)
            else:
                temp.append(0)
        output.append(temp)
    return output

#Driver
def main():
    board, generations = readInput("./inLife.txt")
    generations = int(generations)
    print("Generations to Simulate: " + str(generations))
    print("Generation 0")
    printBoard(board)
    addToFile("./outLife.txt", board, 0)

    for gen in range(generations):
        print("Generation " + str(gen + 1))
        board = getNextGeneration(board)
        printBoard(board)
        addToFile("./outLife.txt", board, gen + 1)

main()
