# Apple Pi Inc.
# Algorithmic Thinking
# Pygame Maze Solver with Depth-First Search Algorithm (DFS)

import pygame
import time

###### set up pygame window ############
WIDTH = 470
HEIGHT = 550

# frames per second, used to slow down the pygame loop
FPS = 30

# define colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# set font size
large_text_size = 20

# initalize pygame
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Python Maze DFS Algorithm")
clock = pygame.time.Clock()

###### setup maze variables ############
# maze is the datastructure storing the barrier/start/end/path locations
# grid represents the visible lines on UI
# visited is the optimization mechanism so the paths are not repeated

solved = False

# x, y are the maze grid offset from the window top left corner
# w is the width of the cell in grid
x = 30                    
y = 30                    
w = 40
maze = []
visited = []
num_rows = 10
num_cols = 10
# DFS needs to find all paths before determine the shortest one
solutions = []

# two barrier values 'barrier1'(default) and 'barrier2'
barrier = 'barrier1'
legendX, legendY = 125, 490
legend_gap = 160
legend_width, legent_height = 50, 50
solveX, solveY = 150, 470
resetX, resetY = 310, 470

# start index
startX = 6
startY = 0

# end index
endX = 3
endY = 9

# images
barrier1_load = pygame.image.load("brick.png")
barrier1 = pygame.transform.scale(barrier1_load, (legent_height, legend_width))
barrier1_rect = barrier1.get_rect(topleft=(legendX,legendY))
barrier1_icon = pygame.transform.scale(barrier1_load, (w-2, w-2))

barrier2_load = pygame.image.load("bush.png")
barrier2 = pygame.transform.scale(barrier2_load, (legent_height, legend_width))
barrier2_rect = barrier2.get_rect(topleft=(legendX+legend_gap,legendY))
barrier2_icon = pygame.transform.scale(barrier2_load, (w-2, w-2))

start_load = pygame.image.load("start.png")
start_icon = pygame.transform.scale(start_load, (w-2, w-2))

end_load = pygame.image.load("end.png")
end_icon = pygame.transform.scale(end_load, (w+11, w+11))

path_load = pygame.image.load("path.png")
path_icon = pygame.transform.scale(path_load, (w-2, w-2))

# solve clickable text
large_text = pygame.font.Font('freesansbold.ttf', large_text_size)
solve_surface = large_text.render("Solve", True, BLACK)
solve_rect = solve_surface.get_rect()

# reset clickable text
reset_surface = large_text.render("Reset", True, BLACK)
reset_rect = reset_surface.get_rect()

# grid clickable area
grid_rect = pygame.Rect(x, y, w * num_rows, w * num_cols)

# mouse coordinates
mouse_x = 0;
mouse_y = 0;

# 2D array (i.e. list of list) to represent maze
def init_maze():
    maze.clear()
    for i in range(1, num_rows+1):
        eachRow = []
        for j in range(1, num_cols+1):
            eachRow.append(0)
        maze.append(eachRow)
    maze[endY][endX] = 20 

# performance optimization
# 2D array (list of list) to keep track of the visited locations
# so that we do not revisit them
def init_visited():
    visited.clear()
    for i in range(1, num_rows+1):
        eachRow = []
        for j in range(1, num_cols+1):
            eachRow.append(0)
        visited.append(eachRow)
        
# draw the grid on UI
def build_grid():
    global x, y
    myX = x
    myY = y

    #draw horizontal lines
    for i in range(0,num_rows + 1):                                                       
        pygame.draw.line(screen, BLACK, [myX, myY], [myX + w*num_cols, myY])
        myY = myY + w

    #draw vertical lines
    myX = x
    myY = y
    for i in range(0,num_cols + 1):                                                       
        pygame.draw.line(screen, BLACK, [myX, myY], [myX, myY + w*num_cols])
        myX = myX + w

def draw_solve_text():
    solve_rect.center = (solveX, solveY)
    screen.blit(solve_surface, solve_rect)

def draw_reset_text():
    reset_rect.center = (resetX, resetY)
    screen.blit(reset_surface, reset_rect)

def draw_barrier1_legend():
    screen.blit(barrier1, (legendX, legendY))

def draw_barrier2_legend():
    screen.blit(barrier2, (legendX + legend_gap, legendY))

def draw_start():
    screen.blit(start_icon, (x+w*startX+1, y+1))

def draw_end():
    screen.blit(end_icon, (x+w*endX, y+w*endY))


# add barriers/start/exit/path icons to the grid area on UI
def draw_maze():
    for i in range(0, num_rows):
        for j in range(0, num_cols):
            
            # fix start and end position
            if i==startY and j == startX:
                screen.blit(start_icon, (x+w*j+1, y+w*i+1))
                
            elif i==endY and j == endX:
                screen.blit(end_icon, (x+w*j-4, y+w*i-4))

            # add barrier
            elif maze[i][j] == 1:
                screen.blit(barrier1_icon, (x+w*j+1, y+w*i+1))
            elif maze[i][j] == 2:
                screen.blit(barrier2_icon, (x+w*j+1, y+w*i+1))                

            # add path
            elif maze[i][j] == 30:
                screen.blit(path_icon, (x+w*j+1, y+w*i+1))


    
def update_path(path):
    j = startX
    i = startY
    pos = set()
    for move in path:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

        # do NOT override exit icon
        if maze[i][j] != 20:
            maze[i][j] = 30


def valid(moves, visited):
    coordinate = find_coordinate(moves)
    i = coordinate[0]
    j = coordinate[1]
    
    # if outside of boundary
    if not(0 <= j < len(maze[0]) and 0 <= i < len(maze)):
        return False
    
    # if road block
    elif (maze[i][j] > 0 and maze[i][j] < 10):
        return False
    
    # if visited
    elif (visited[i][j] == 1):
        return False

    return True


# convert location steps ((e.g.DLLDR) to row/column indexes
def find_coordinate(moves):
    j = startX
    i = startY
    for move in moves:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1

    return (i, j)

def find_end(moves):
    global solutions
    
    coordinate =find_coordinate(moves)
    i = coordinate[0]
    j = coordinate[1]
    
    if (0 <= i < num_rows) and (0 <= j < num_cols) and maze[i][j] == 20:
        solutions.append(moves)
        return True
    return False

# using DFS to find shortest path has to
# traverse through all possible paths and pick the
# shortest one
# the two parameters are used to maintain the local context (stack)
def solve_maze_recur(moves, visited):
    # base case
    if find_end(moves):
        return 
    
    if not valid(moves, visited):
        return

    coordinate = find_coordinate(moves)
    i = coordinate[0]
    j = coordinate[1]

    # clone the visited 2D array
    # so that it maintain the local context
    # instead of updating the global visited
    # in order to find the next path
    new_visited = list(map(list, visited))
    new_visited[i][j] = 1
    
    solve_maze_recur(moves + 'L', new_visited)
    solve_maze_recur(moves + 'R', new_visited)    
    solve_maze_recur(moves + 'U', new_visited)
    solve_maze_recur(moves + 'D', new_visited)

def solve_maze():
    solve_maze_recur('', visited)
    minLength = 999999
    shortest_path = ''
    for sol in solutions:
        if (len(sol) < minLength):
            minLength = len(sol)
            shortest_path = sol
    print('Total paths: ' + str(len(solutions)))
    print('Shortest: ' + shortest_path, end='')
    update_path(shortest_path)

def start_game():
    screen.fill(WHITE)
    init_maze()
    init_visited()
    build_grid()
    draw_solve_text()
    draw_reset_text()
    draw_barrier1_legend()
    draw_barrier2_legend()
    draw_start()
    draw_end()
    pygame.display.update()

                
start_game()


# pygame loop
running = True
while running:
    # slow down the while loop based on FPS
    clock.tick(FPS)
    
    # process input (events)
    for event in pygame.event.get():
        
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

        # position of the mouse                     
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:

            # once the maze is solved, can only click reset 
            if solved:

                if reset_rect.collidepoint(event.pos):
                    start_game()
                    solved = False

            else:
                col_num = (int)((mouse_x-x)/w)
                row_num = (int)((mouse_y-y)/w)
                
                if solve_rect.collidepoint(event.pos):
                    solve_maze()

                elif reset_rect.collidepoint(event.pos):
                    start_game()
                    
                # selection of legands
                elif barrier1_rect.collidepoint(event.pos):
                    barrier = "barrier1"
                
                elif barrier2_rect.collidepoint(event.pos):
                    barrier = "barrier2"

                elif (grid_rect.collidepoint(event.pos) and 
                    not (row_num == startY and col_num == startX) and
                    not (row_num == endY and col_num == endX)):
                    
                    if (barrier == "barrier1"):
                        maze[row_num][col_num] = 1
                    elif (barrier == "barrier2"):
                        maze[row_num][col_num] = 2

            draw_maze()
            pygame.display.update()

pygame.quit()
