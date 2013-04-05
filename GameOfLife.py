from time import sleep

n = 30
time = 0
endingTime = 200

gridOne = [[0]*n for i in range(n)]
gridTwo = [row[:] for row in gridOne]

gridOne[9][9] = 1
gridOne[9][10] = 1
gridOne[9][13] = 1
gridOne[9][14] = 1
gridOne[9][15] = 1

gridOne[8][12] = 1
gridOne[7][10] = 1




currentGrid = gridOne
otherGrid = gridTwo
  
def transition(i, j):
    num_neighbors = 0
    # Gather top neighbors not on top row
    if i != 0:
        # Gather top left neighbor if leftmost column
        if j != 0:
            num_neighbors += currentGrid[i-1][j-1]
        num_neighbors += currentGrid[i - 1][j]
        # Gather top right neighbor if not in rightmost column
        if j != n - 1:
            num_neighbors += currentGrid[i-1][j+1]
    # Gather left neighbor if it exists
    if j != 0:
        num_neighbors += currentGrid[i][j-1]
    # Gather right neighbor if it exists
    if j != n - 1:
        num_neighbors += currentGrid[i][j+1]
    # Gather bottom neighbors not on bottom row
    if i != n - 1:
        # Gather bottom left neighbor if not in bottom left corner
        if j != 0:
            num_neighbors += currentGrid[i+1][j-1]
        num_neighbors += currentGrid[i + 1][j]
        # Gather top right neighbor not in top right corner
        if j != n - 1:
            num_neighbors += currentGrid[i+1][j+1]
    # Protocol for dead cell
    if not currentGrid[i][j]:
        if num_neighbors == 3:
            otherGrid[i][j] = 1
        else:
            otherGrid[i][j] = 0
    #Protocol for alive cell
    else:
        if  2 <= num_neighbors <= 3:
            otherGrid[i][j] = 1
        else:
            otherGrid[i][j] = 0
print "Start"
for row in currentGrid:
        print row
sleep(5)
while time <= endingTime:
    for i in range(n):
        for j in range(n):
            transition(i,j)
    temp = currentGrid
    currentGrid = otherGrid
    otherGrid = temp
    time += 1
    print "time", time
    for row in currentGrid:
            print row
    sleep(.2)
    
