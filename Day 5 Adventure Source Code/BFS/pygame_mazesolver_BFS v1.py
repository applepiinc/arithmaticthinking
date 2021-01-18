# Apple Pi Inc.
# Algorithmic Thinking
# Pygame Maze Solver with Breadth-First Search Algorithm (BFS)

import pygame
import time
import queue

###### set up pygame window ############
WIDTH = 1050
HEIGHT = 745

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
pygame.display.set_caption("Python Maze BFS Algorithm")
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
num_rows = 15
num_cols = 15

# two barrier values 'wall'(default) and 'grass'
barrier = 'wall'
legendX, legendY = 195, 670
legend_gap = 155
legend_width, legent_height = 50, 50
solveX, solveY = 200, 650
resetX, resetY = 400, 650

# fix start index: first row, 12th column
startX = 11
startY = 0

# fix end index:  15th row, 4th column
endX = 3
endY = 14

# images
wall_load = pygame.image.load("wall.png")
wall = pygame.transform.scale(wall_load, (legent_height, legend_width))
wall_rect = wall.get_rect(topleft=(legendX,legendY))
wall_icon = pygame.transform.scale(wall_load, (w-2, w-2))

grass_load = pygame.image.load("grass.png")
grass = pygame.transform.scale(grass_load, (legent_height, legend_width))
grass_rect = grass.get_rect(topleft=(legendX+legend_gap,legendY))
grass_icon = pygame.transform.scale(grass_load, (w-2, w-2))

start_load = pygame.image.load("start.png")
start_icon = pygame.transform.scale(start_load, (w-2, w-2))

end_load = pygame.image.load("end.png")
end_icon = pygame.transform.scale(end_load, (w+11, w+11))

path_load = pygame.image.load("path.jpg")
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

def draw_wall_legend():
    screen.blit(wall, (legendX, legendY))

def draw_grass_legend():
    screen.blit(grass, (legendX + legend_gap, legendY))

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
                screen.blit(wall_icon, (x+w*j+1, y+w*i+1))
            elif maze[i][j] == 2:
                screen.blit(grass_icon, (x+w*j+1, y+w*i+1))                

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


def valid(moves):
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
    coordinate =find_coordinate(moves)
    i = coordinate[0]
    j = coordinate[1]
    
    if maze[i][j] == 20:
        update_path(moves)
        return True

    return False

def solve_maze():
    global solved

    # queue is important data structure to BFS
    # it keeps track of the next locations to explore in order
    steps = queue.Queue()

    # add start location to queue
    # '' steps needed from itself
    steps.put("")
    current_pos = ""

    # set start position to be visited,
    visited[startY][startX] = 1
    
    while not solved:

        current_pos = steps.get()
        
        for neighbour in ["L", "R", "U", "D"]:
            
            next_pos = current_pos + neighbour
            
            if valid(next_pos):
                    
                if find_end(next_pos):
                    solved = True
                    
                else:
                    steps.put(next_pos)

                    i, j = find_coordinate(next_pos)
                    visited[i][j] = 1


def start_game():
    screen.fill(WHITE)
    init_maze()
    init_visited()
    build_grid()
    draw_solve_text()
    draw_reset_text()
    draw_wall_legend()
    draw_grass_legend()
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
                elif wall_rect.collidepoint(event.pos):
                    barrier = "wall"
                
                elif grass_rect.collidepoint(event.pos):
                    barrier = "grass"

                elif (grid_rect.collidepoint(event.pos) and 
                    not (row_num == startY and col_num == startX) and
                    not (row_num == endY and col_num == endX)):
                    
                    if (barrier == "wall"):
                        maze[row_num][col_num] = 1
                    elif (barrier == "grass"):
                        maze[row_num][col_num] = 2

            draw_maze()
            pygame.display.update()

pygame.quit()
