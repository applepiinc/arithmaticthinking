# Apple Pi Inc.
# Algorithmic Thinking
# Pygame Golden Spiral based on Fibonacci Numbers

import pygame 
import math 

###### set up pygame window ############
WIDTH = 900
HEIGHT = 600

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
screen.fill(WHITE)
pygame.display.set_caption("Python Fibonacci Golden Spiral")
pygame.display.flip()
clock = pygame.time.Clock()

###### setup plot variables ############
x = int(WIDTH/2)
y = int(HEIGHT/2)
dot_radius = 3

def plot_spiral(n):
    # generate the first n fibonacci numbers
    fibonacci(n)

    # draw spiral for the first 10 squares
    start_x = x
    start_y = y

    # 0 to n+1 because end index is exclusive
    for i in range(0, n+1): 
        print(fib[i])
        pygame.draw.circle(screen, (137,207,240), [start_x, start_y], 5, 0)
        pygame.display.update()
        pygame.time.delay(1000)      

                           
        #bottom right start
        if (i%4 == 1):
            curr_x = start_x - fib[i]
            curr_y = start_y - fib[i]

        #top right start
        elif (i%4 == 2):
            curr_x = start_x - fib[i]
            curr_y = start_y

        #top left start
        elif (i%4 == 3):
            curr_x = start_x
            curr_y = start_y

        # bottom left start
        else:
            curr_x = start_x
            curr_y = start_y - fib[i]
        rect = pygame.draw.rect(screen, BLACK, [curr_x, curr_y, fib[i], fib[i]], 2)

        # center of the quadrant
        arc_x = 0
        arc_y = 0

        #bottom right start
        if (i%4 == 1):
            arc_x = start_x - 2 * fib[i]
            arc_y = start_y - fib[i]
            #rect = pygame.draw.rect(screen, BLACK, [arc_x, arc_y, 2 * fib[i], 2 * fib[i]], 2)
            pygame.draw.arc(screen, BLACK, [arc_x, arc_y, 2 * fib[i], 2 * fib[i]], 0, math.pi/2, 2)

           
            start_x = start_x - fib[i]
            start_y = start_y - fib[i]

        #top right start
        elif (i%4 == 2):
            arc_x = start_x - fib[i]
            arc_y = start_y
            pygame.draw.arc(screen, BLACK, [arc_x, arc_y, 2 * fib[i], 2 * fib[i]], math.pi/2, math.pi, 2)

            start_x = start_x - fib[i]
            start_y = start_y + fib[i]

        #top left start
        elif (i%4 == 3):
            arc_x = start_x
            arc_y = start_y - fib[i]
            pygame.draw.arc(screen, BLACK, [arc_x, arc_y, 2 * fib[i], 2 * fib[i]], math.pi, math.pi*3/2, 2)

            start_x = start_x + fib[i]
            start_y = start_y + fib[i]

        # bottom left start
        else:
            arc_x = start_x - fib[i]
            arc_y = start_y - 2 * fib[i]
            pygame.draw.arc(screen, BLACK, [arc_x, arc_y, 2 * fib[i], 2 * fib[i]], math.pi*3/2, math.pi*2, 2)

            start_x = start_x + fib[i]
            start_y = start_y - fib[i]

        pygame.display.update()
        pygame.time.delay(800)      

        pygame.draw.circle(screen, (137,207,240), [start_x, start_y], 5, 0)
        pygame.display.update()
        pygame.time.delay(1000)      
        
  
# Here 'factor' signifies the multiplicative  
# factor which expands or shrinks the scale 
# of the plot by a certain factor. 
factor = 5
fib = []

def fibonacci(n):
    global fib
    for i in range(n+1):
        fib.append(0)

    fib_recur(n)

    # print fib numbers to console
    for f in fib:
        print(f, end=" ")
    print()
    
# recursive function
def fib_recur(n):
    global fib
    
    # base case to stop the recursion call
    if (n==0):
        fib[n] = 0
        return 0
    if (n==1):
        fib[n] = 1
        return 1

    # compute fib number
    fib_n = fib_recur(n-1) + fib_recur(n-2)
    fib[n] = fib_n
    return fib_n

    
# pygame loop to continuously take user input
running = True
while running:
    # slow down the while loop based on FPS
    clock.tick(FPS*100)
    
    # process input (events)
    for event in pygame.event.get():
        
        # check for closing window
        if event.type == pygame.QUIT:
            running = False

        # position of the mouse                     
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if event.type == pygame.MOUSEBUTTONDOWN:
            print(mouse_x)
            print(mouse_y)
            plot_spiral(11)

        # update the entire screen
        pygame.display.update()
                
pygame.quit()

