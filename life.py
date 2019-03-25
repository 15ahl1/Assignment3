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
    xLen = len(board[0])
    yLen = len(board)
    count = 0
    #Up
    if board[x][y - 1] == 1:
        count += 1
    #Down
    if board[x][y + 1] == 1:
        count += 1
    #Left
    if board[x - 1][y] == 1:
        count += 1
    #Right
    if board[x + 1][y] == 1:
        count += 1
    #TopLeft
    if board[x - 1][y - 1] == 1:
        count += 1
    #TopRight
    if board[x + 1][y - 1] == 1:
        count += 1
    #BottomLeft
    if board[x - 1][y + 1] == 1:
        count += 1
    #BottomRight
    if board[x + 1][y + 1] == 1:
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


#def nextGeneration(board):




def main():
    board, generations = readInput("./inLife.txt")
    print("Generations to Simulate: " + generations)
    print("Generation 0")
    printBoard(board)
    addToFile("./outLife.txt", board, 0)
    '''
    for gen in range(generations):
        print("Generation " + (gen + 1))
        board = getNextGeneration(board)
        printBoard(board)
        addToFile("./outLife.txt", board, gen + 1)
    '''


main()
