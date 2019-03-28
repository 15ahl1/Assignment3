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
    global allBoards
    global generations
    global currentGen
    currentGen = 0

    allBoards = []
    board, generations = readInput("inLife.txt")
    generations = int(generations)
    print("Generations to Simulate: " + str(generations))
    print("Generation 0")
    printBoard(board)
    addToFile("outLife.txt", board, 0)
    allBoards.append(board)

    for gen in range(generations):
        print("Generation " + str(gen + 1))
        board = getNextGeneration(board)
        printBoard(board)
        addToFile("./outLife.txt", board, gen + 1)
        allBoards.append(board)
    
            
#Setup window for GUI
def setup():
    size(900, 1000)
    f = loadFont("Text.vlw")
    textFont(f, 30)
    fill(0)
    textAlign(CENTER)
    main()



def draw():
    fill(255)
    rect(0, 0, width, height)
    fill(200)
    rect(0, 0, width, height - 100)
    fill(0)
    global currentGen, generations, allBoards
    next = text("Next\n ->",  width - width / 4, height - height / 18)
    previous = text("Previous\n <-", width / 4, height - height / 18)
    
    text(str(currentGen) + "/" + str(generations), width / 2, height - height / 20)
    
    if keyPressed:
        if keyCode == RIGHT and currentGen < generations:
            currentGen += 1
        elif keyCode == LEFT and currentGen > 0:
            currentGen -= 1
        delay(200)
    
    drawGrid(currentGen)
        
 
def drawGrid(gen):
    global allBoards
    board = allBoards[gen]
    
    rows = len(board)
    cols = len(board[0])
    
    for y in range(0, rows):
        for x in range(0, cols):
            if board[y][x] == 1:
                fill(0)
            elif board[y][x] == 0:
                fill(255)
            rect(x * (900/cols), y * (900/rows), 900/cols, 900/rows)
    
