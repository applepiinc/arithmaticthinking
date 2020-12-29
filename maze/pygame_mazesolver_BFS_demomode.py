# Apple Pi Inc.
# Algorithmic Thinking
# Pygame Maze Solver Demo with Breadth-First Search Algorithm

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


###### demo mode setup  ############
# default to play model
demo_mode = False
demoX, demoY = 720, 100
playX, playY = 840, 100
queueX, queueY = 640, 300
medium_text_size = 15
small_text_size = 10
LIGHTGREY = (192, 192, 192)

medium_text = pygame.font.Font('freesansbold.ttf', medium_text_size)
demo_surface = medium_text.render("Demo Mode", True, BLACK)
demo_rect = demo_surface.get_rect()

play_surface = medium_text.render("Play Mode", True, LIGHTGREY)
play_rect = play_surface.get_rect()

small_text = pygame.font.Font('freesansbold.ttf', small_text_size)
step_num = 0
has_left = False
has_right = False
has_up = False
has_down = False
step_surface = small_text.render(str(step_num), True, BLACK)
step_rect = step_surface.get_rect()

neighbour_surface = medium_text.render("L", True, BLACK)
neighbour_rect = neighbour_surface.get_rect()

def draw_mode():
    global demo_surface, demo_rect, play_surface, play_rect
    if demo_mode:
        demo_surface = medium_text.render("Demo Mode", True, BLACK)
        demo_rect = demo_surface.get_rect()

        play_surface = medium_text.render("Play Mode", True, LIGHTGREY)
        play_rect = play_surface.get_rect()
        
    else:
        demo_surface = medium_text.render("Demo Mode", True, LIGHTGREY)
        demo_rect = demo_surface.get_rect()

        play_surface = medium_text.render("Play Mode", True, BLACK)
        play_rect = play_surface.get_rect()
        
    demo_rect.center = (demoX, demoY)
    screen.blit(demo_surface, demo_rect)

    play_rect.center = (playX, playY)
    screen.blit(play_surface, play_rect)

###### end demo mode setup ############
    

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

    ### demo mode ###
    draw_mode()
    ### end demo mode ###
    
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

### demo mode ###
def get_all_coordinates(steps):
    coord_str = ""
    for step in steps.queue:
        i, j = find_coordinate(step)
        coord_str = coord_str + "(" + str(i) + "," + str(j) + ") "
    return coord_str
### end demo mode ###

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
    steps = queue.Queue()
    steps.put("")
    current_pos = ""
    
    # set start position to be visited,
    visited[startY][startX] = 1

    ### demo mode ###
    if demo_mode:
        global step_num, has_left,has_right,has_up,has_down
        global step_left_surface, step_left_rect, step_right_surface, step_right_rect
        global step_up_surface, step_up_rect, step_down_surface, step_down_rect
    ### end model mode ###
    
    while not solved:

        current_pos = steps.get()

        ### demo mode ###
        if demo_mode:
            currentI, currentJ = find_coordinate(current_pos)

            # black location: its neighbourhood is being explored
            exploring_rect = pygame.Rect(x+w*currentJ+11, y+w*currentI+11, w-17, w-17)
            pygame.draw.rect(screen, BLACK, exploring_rect)
            pygame.display.update()
            #pygame.time.delay(800)
            pygame.time.delay(100)
        ### end demo mode ###
        
        for neighbour in ["L", "R", "U", "D"]:
            
            next_pos = current_pos + neighbour
            
            if valid(next_pos):
                    
                if find_end(next_pos):
                    solved = True
                    
                else:
                    steps.put(next_pos)

                    i, j = find_coordinate(next_pos)
                    visited[i][j] = 1

                    ### demo mode ###
                    if demo_mode:
                        
                        # show content in queue
                        pygame.draw.rect(screen, WHITE, (queueX, queueY, 410, 25))
                        queue_str = get_all_coordinates(steps)
                        queue_surface = medium_text.render("Queue: " + queue_str, True, BLACK)
                        queue_rect = queue_surface.get_rect()
                        queue_rect.topleft = (queueX, queueY)
                        screen.blit(queue_surface, queue_rect)

                        # lightblue: location putting in the queue
                                                                    
                        if neighbour == "L":
                            has_left = True
                            rect_left = pygame.Rect(x+w*j+11, y+w*i+11, w-17, w-17)
                            pygame.draw.rect(screen, (137,207,240), rect_left)
                        
                        elif neighbour == "R":
                            has_right = True
                            rect_right = pygame.Rect(x+w*j+11, y+w*i+11, w-17, w-17)
                            pygame.draw.rect(screen, (137,207,240), rect_right)

                        elif neighbour == "U":
                            has_up = True
                            rect_up = pygame.Rect(x+w*j+11, y+w*i+11, w-17, w-17)
                            pygame.draw.rect(screen, (137,207,240), rect_up)
                            
                        elif neighbour == "D":
                            has_down = True
                            rect_down = pygame.Rect(x+w*j+11, y+w*i+11, w-17, w-17)
                            pygame.draw.rect(screen, (137,207,240), rect_down)

                        step_num = step_num + 1
                        step_surface = small_text.render(str(step_num), True, BLACK)
                        step_rect.topleft = (x+w*j+3, y+w*i+3)
                        screen.blit(step_surface, step_rect)

                        neighbour_surface = small_text.render(neighbour, True, BLACK)
                        neighbour_rect.topleft = (x+w*j+18, y+w*i+18)
                        screen.blit(neighbour_surface, neighbour_rect)
                        
                        pygame.display.update()
                        #pygame.time.delay(800)
                        pygame.time.delay(100)

        
        ### demo mode ###
        if demo_mode:
            # grey: location removed from the queue, finished exploring the neighbourhood
            # pause to show location (black) and its neighbours (lighblue)
            #pygame.time.delay(1600)
            pygame.time.delay(100)
            pygame.draw.rect(screen, LIGHTGREY, exploring_rect)

            if has_left:
                pygame.draw.rect(screen, (137,207,240), rect_left)

            if has_right:
                pygame.draw.rect(screen, (137,207,240), rect_right)
            if has_up:
                pygame.draw.rect(screen, (137,207,240), rect_up)
            if has_down:
                pygame.draw.rect(screen, (137,207,240), rect_down)

            has_left = False
            has_right = False
            has_up = False
            has_down = False
            
            pygame.display.update()
            #pygame.time.delay(800)
            pygame.time.delay(100)
        ### end demo mode ###

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
    draw_mode()
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

                ### demo mode ###
                elif demo_rect.collidepoint(event.pos):
                    demo_mode = True

                elif play_rect.collidepoint(event.pos):
                    demo_mode = False
                ### end demo mode ###

            draw_maze()
            pygame.display.update()

pygame.quit()
