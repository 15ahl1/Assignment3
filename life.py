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

def printBoard(board):
    for row in board:
        for elem in row:
            print(elem),
        print("\n")

def calculateLiveNeighbours(board, x, y):
    count = 0
    xLen = len(board[0])
    yLen = len(board)
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

    print("Calculated Neighbours: " + str(count))
    return count

def addToFile(path, board, gen):
    with open(path, "a") as file:
        file.write(str(gen) + "\n")
        for row in board:
            temp = ""
            for elem in row:
                temp += (str(elem) + "")
            file.write(temp + "\n")
    file.close()

def onOffTable(board):
    xLen = len(board[0])
    yLen = len(board)
    output = []
    for row in range(yLen):
        temp = []
        for elem in range(xLen):
            temp.append(calculateLiveNeighbours(board, elem, row))
        output.append(temp)
    return output


def getNextGeneration(board):
    liveTable = onOffTable(board)
    printBoard(liveTable)
    print("\n")
    output = []
    for i in range(len(board[0])):
        temp = []
        for j in range(len(board)):
            if(liveTable[i][j] >= 2 and board[i][j] == 1):
                temp.append(1)
            elif(liveTable[i][j] >= 3):
                temp.append(1)
            else:
                temp.append(0)
        output.append(temp)
    return output




def main():
    board, generations = readInput("./inLife.txt")
    print("Generations to Simulate: " + generations)
    print("Generation 0")
    printBoard(board)
    addToFile("./outLife.txt", board, 0)
    next = getNextGeneration(board)
    printBoard(next)
    '''
    for gen in range(generations):
        print("Generation " + (gen + 1))
        board = getNextGeneration(board)
        printBoard(board)
        addToFile("./outLife.txt", board, gen + 1)
    '''


main()
