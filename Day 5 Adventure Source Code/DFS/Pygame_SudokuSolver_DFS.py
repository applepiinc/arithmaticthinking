import pygame
import time

###### set up pygame window ############
WIDTH = 1050
HEIGHT = 745

# frames per second, used to slow down the pygame loop
FPS = 30

# define colours
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREY = (50, 50, 50)
LIGHTGREY = (192, 192, 192)

# initalize Pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Sudoku Puzzle DFS Algorithm")
clock = pygame.time.Clock()

###### setup grid variables ############
# grid represents the visible lines on UI
# x, y are the grid offset from the window top left corner
# w is the width of the cell in grid
x = 30                    
y = 30                    
w = 40
numRows = 9
numCols = 9
s =[]
largeText = pygame.font.Font('freesansbold.ttf', 20)
stepSurface = largeText.render(str(0), True, BLACK)
stepRect = stepSurface.get_rect()


def createPuzzle():
    global s
    s = [[3, 0, 9, 0, 0, 0, 4, 0, 0],
             [2, 0, 0, 7, 0, 9, 0, 0, 0],
             [0, 8, 7, 0, 0, 0, 0, 0, 0],
             [7, 5, 0, 0, 6, 0, 2, 3, 0],
             [6, 0, 0, 9, 0, 4, 0, 0, 8],
             [0, 2, 8, 0, 5, 0, 0, 4, 1],
             [0, 0, 0, 0, 0, 0, 5, 9, 0],
             [0, 0, 0, 1, 0, 6, 0, 0, 7],
             [0, 0, 6, 0, 0, 0, 1, 0, 4]]
    
# draw the grid on UI
def buildGrid():
    global x, y
    myX = x
    myY = y

    #draw horizontal lines
    for i in range(0,numRows + 1):
        if i in [3, 6]:
            pygame.draw.line(screen, BLUE, [myX, myY], [myX + w*numCols, myY], width=4)
        else:
            pygame.draw.line(screen, BLACK, [myX, myY], [myX + w*numCols, myY], width=1)
        myY = myY + w

    #draw vertical lines
    myX = x
    myY = y
    for i in range(0,numCols + 1):
        if i in [3, 6]:
            pygame.draw.line(screen, BLUE, [myX, myY], [myX, myY + w*numCols], width=4)
        else:
            pygame.draw.line(screen, BLACK, [myX, myY], [myX, myY + w*numCols], width=1)
        myX = myX + w

def drawPuzzle():
    for i in range(0, numRows):
        for j in range(0, numCols):
            if (s[i][j] != 0):
                stepSurface = largeText.render(str(s[i][j]), True, BLACK)
                stepRect.topleft = (x+w*j+10, y+w*i+10)
                screen.blit(stepSurface, stepRect)
                

def print_sudoku(s):
    for row in range(9):
        for col in range(9):
            print(s[row][col], end=' ')
            if col+1 == 3 or col+1 == 6:
                print(" | ", end=' ')
        if row+1 == 3 or row+1 == 6:
            print("\n" + "-"*25, end=' ')
        print()
    print()

# return a list representing the used numbers
# 0 = not used, 1 = used
def get_used_numbers(s, row, col):

    used = [0]*10
    used[0] = 1

    block_row = row // 3
    block_col = col // 3
    
    # mark the used numbers in the same row, column
    for i in range(9):
        used[s[i][col]] = 1;
        used[s[row][i]] = 1;

    # mark the used numbers in the connected block
    for i in range(3):
        for j in range(3):
            used[s[i + block_row*3][j + block_col*3]] = 1

    return used

# try to fill in the cells that only have one possibility (low hanging fruit!)
# go through number of passes as long as there are easy fills.
def initial_try(s):
    easy_fill = True

    while easy_fill:
        easy_fill = False
        
        # check each cell of the puzzle
        for row in range(9):
            for col in range(9):

                # only try when current cell is empty
                if s[row][col] == 0:
                    used = get_used_numbers(s, row, col)
                
                    # if only one possibility, fill it
                    if used.count(0) == 1:
                        easy_fill = True

                        s[row][col] = used.index(0)

# DFS algorithm
def DFS_solve(s, row, col):
    # base case: fill in the last cell
    if row == 8 and col == 8:
        used = get_used_numbers(s, row, col)
        if 0 in used:
            s[row][col] = used.index(0)
        return True

    # once finishing the current row, move to the next row
    if col == 9:
        row = row+1
        col = 0

    # when current cell is not empty, directly move to the next
    if s[row][col] != 0:
        return DFS_solve(s, row, col+1)

    # work on the empty cell
    if s[row][col] == 0:
        used = get_used_numbers(s, row, col)

        # this for loop is the DFS key
        # 
        for i in range(1, 10):
            if used[i] == 0:

                # solve the current cell and move to the next cell
                s[row][col] = i
                if DFS_solve(s, row, col+1):
                    return True

        # Reached here? Then we tried 1-9 without success
        s[row][col] = 0
        return False
    

def main():
    start = time.time()
    num_puzzles = 0
    text = ""

    solved = False
        
    print("Original:")
    print_sudoku(s)

    used = get_used_numbers(s, 7, 7)
    for m in range(10):
        print(str(m) + str(used[m]))

    initial_try(s)
    DFS_solve(s, 0, 0)

    print("Solution:")
    print_sudoku(s)

    print("="*30)

    print("{:.2f} seconds to solve the puzzle".format(time.time() - start))
    

def startGame():
    screen.fill(WHITE)
    createPuzzle()
    buildGrid()
    drawPuzzle()
    pygame.display.update()

    pygame.time.delay(1600)
    start = time.time()
    DFS_solve(s, 0, 0)
    end = time.time()
    print("{:.2f} seconds to solve the puzzle".format(end - start))
    drawPuzzle()
    pygame.display.update()

                
startGame()

