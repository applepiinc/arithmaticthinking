# Apple Pi Inc.
# Algorithmic Thinking
# Node

import pygame

###### setup pygame window ############
WIDTH = 900
HEIGHT = 600

# frames per second, used to slow down the pygame loop
FPS = 30

# define colours
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
LIGHT_BROWN = (126, 94, 62)
BROWN = (107, 62, 35)

# initialize pygame
pygame.init()
# create a canvas for the desired dimension
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

pygame.display.set_caption("Python Node")
pygame.display.flip()
clock = pygame.time.Clock()

largeText = pygame.font.SysFont('comicsansms', 30)
mediumText = pygame.font.SysFont('comicsansms', 25)

###### setup Node variables ############
nodeNum = 1
nodeList = []
nodeRadius = 16

class Node:
    x: int
    y: int
    nodeNum: int

    # constructor
    # a. called when creating an object of type Node
    # b. purpose is to initialize instance variables
    # c. always named __init__
    # d. first parameter 'self' allows accessing the instance variables
    def __init__(self, x: int, y: int, nodeNum: int):
        # use keyword 'self' to refer to instance variables
        self.x = x
        self.y = y
        self.nodeNum = nodeNum
        
def drawNode(node):
    # draw node circle centered at (node.x, node.y)
    pygame.draw.circle(screen, LIGHT_BROWN, (node.x, node.y), nodeRadius)

    # draw the node number
    nodeSurface = largeText.render(str(node.nodeNum), True, WHITE)
    # define the rect value of the nodeSurface centered in the circle
    nodeRect = nodeSurface.get_rect(center=(node.x, node.y))
    # draw the node number on the screen at the rect position      
    screen.blit(nodeSurface, nodeRect)
    
def drawInstruction():
    # box dimension: topleft (50, 110), bottomright (750, 440)
    pygame.draw.rect(screen, BROWN, pygame.Rect(50, 110, 700, 330), 2)
    instructOneLabel_Surface = mediumText.render('Click Inside Box to Add Nodes', True, BLACK)
    screen.blit(instructOneLabel_Surface, (50, 460))

def startGame():
    drawInstruction()
    pygame.display.update()

# pygame loop to continuously take user input
running = True

startGame()

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

            # draw nodes when clicking inside the box
            # box dimension: topleft (50, 110), bottomright (750, 440)
            # leave edge of radius size
            # if (mouse_x > 60 and mouse_x < 740) and
            #    (mouse_y > 120 and mouse_y <430):
            if (mouse_x > 50+nodeRadius and mouse_x < 750-nodeRadius) \
                and (mouse_y > 110+nodeRadius and mouse_y <440-nodeRadius):
                # add new node to the list
                nodeList.append(Node(mouse_x, mouse_y, nodeNum))

                # draw new node
                # using list here for graph processing in the next step
                drawNode(Node(mouse_x, mouse_y, nodeNum))

                # increase node number by 1
                nodeNum += 1

        # update the entire screen
        pygame.display.update()
                
pygame.quit()

    

