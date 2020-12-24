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

pygame.display.set_caption("Python Graph")
pygame.display.flip()
clock = pygame.time.Clock()

largeText = pygame.font.SysFont('comicsansms', 30)
mediumText = pygame.font.SysFont('comicsansms', 25)

###### setup Graph variables ############

# variables for edge & weight input fields

# srcNode label coordinate
srcX, srcY = 50, 50
# dstNode label coordinate
dstX, dstY = 150, 50
# weight label coordinate
weightX, weightY = 250, 50
# 'Add Edge' label coordinate
setX, setY = 350, 50

# srcNode input box
srcText = ''
srcText_surface = largeText.render("{:<8}".format('  ' + srcText), True, BLACK)
srcText_rect = srcText_surface.get_rect()
pygame.draw.rect(srcText_surface, BLACK, srcText_rect, 2) 

# dstNode input box
dstText = ''
dstText_surface = largeText.render("{:<8}".format('  ' + dstText), True, BLACK)
dstText_rect = dstText_surface.get_rect()
pygame.draw.rect(dstText_surface, BLACK, dstText_rect, 2) 

# weight input box
weightText = ''
weightText_surface = largeText.render("{:<8}".format('  ' + weightText), True, BLACK)
weightText_rect = weightText_surface.get_rect()
pygame.draw.rect(weightText_surface, BLACK, weightText_rect, 2)

# set clickable text
addEdgeSurface = largeText.render("Add Edge", True, BLACK)
addEdgeRect = addEdgeSurface.get_rect()

# initialize the input number
srcNodeNum = -1
dstNodeNum = -1
weightNum = -1

# variables for node
nodeNum = 1
nodeList = []
edgeList = []
nodeRadius = 16

# mode represents which field is being modified by user
# 'setSrc', 'setDst', 'setWeight', 'clear'
mode = ''

class Node:
    # instance variables
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

class Edge:
    # instance variables
    src: Node
    dst: Node
    weight: int

    # constructor
    def __init__(self, src: Node, dst: Node, weight: int):
        self.src = src
        self.dst = dst
        self.weight = weight

class Graph:
    # instance variables
    nodeList: list
    edgeList: list
    
    # constructor
    def __init__(self, nodeList: int, edgeList: list):
        self.nodeList = nodeList
        self.edgeList = edgeList

def drawNode(node):
    # draw node circle centered at (node.x, node.y)
    pygame.draw.circle(screen, LIGHT_BROWN, (node.x, node.y), nodeRadius)

    # draw the node number
    nodeSurface = largeText.render(str(node.nodeNum), True, WHITE)
    # define the rect value of the nodeSurface centered in the circle
    nodeRect = nodeSurface.get_rect(center=(node.x, node.y))
    # draw the node number on the screen at the rect position      
    screen.blit(nodeSurface, nodeRect)

def drawNodes(nodes):
    for node in nodes:
        drawNode(node)
    
def drawEdge(edge, color, edgeWidth):
    edgeSrcX, edgeSrcY = edge.src.x, edge.src.y
    edgeDstX, edgeDstY = edge.dst.x, edge.dst.y
    weight = edge.weight
    pygame.draw.line(screen, color, (edgeSrcX, edgeSrcY), (edgeDstX, edgeDstY), width=edgeWidth)
    # only draw weight number when not zero
    if weight !=0:
        weightLabel_Surface = largeText.render(str(weight), True, color)
        weightLabelX = int((edgeSrcX + edgeDstX)/2)
        weightLabelY = int((edgeSrcY + edgeDstY)/2)

        # when edge is tilted from topleft to bottomright
        # make sure weight number not overlapping with edge line
        if ((edgeSrcX-edgeDstX) * (edgeSrcY-edgeDstY) > 0):
            weightLabelX -= 9
        else:
            weightLabelX += 3
            weightLabelY += 3
        screen.blit(weightLabel_Surface, (weightLabelX, weightLabelY))

def drawEdges(edges, color, edgeWidth):
    for edge in edges:
        drawEdge(edge, color, edgeWidth)
        
def drawWeightInput():
    srcLabel_Surface = mediumText.render("Src Node #", True, BLACK)
    screen.blit(srcLabel_Surface, (srcX, srcY))
    srcText_rect.topleft = (srcX, srcY+20)
    screen.blit(srcText_surface, srcText_rect)
    
    dstLabel_Surface = mediumText.render("Dst Node #", True, BLACK)
    screen.blit(dstLabel_Surface, (dstX, dstY))
    dstText_rect.topleft = (dstX, dstY+20)
    screen.blit(dstText_surface, dstText_rect)

    weightLabel_Surface = mediumText.render("Weight", True, BLACK)
    screen.blit(weightLabel_Surface, (weightX, weightY))
    weightText_rect.topleft = (weightX, weightY+20)
    screen.blit(weightText_surface, weightText_rect)

    addEdgeRect.topleft = (setX, setY)
    screen.blit(addEdgeSurface, addEdgeRect)

def drawInstruction():
    # box dimension: topleft (50, 110), bottomright (750, 440)
    pygame.draw.rect(screen, BROWN, pygame.Rect(50, 110, 700, 330), 2)
    instructOneLabel_Surface = mediumText.render('Step 1: Click Inside Box to Add Nodes', True, BLACK)
    screen.blit(instructOneLabel_Surface, (50, 460))

    instructTwoLabel_Surface = mediumText.render('Step 2: Enter Src Node #, Dst Node # and Weight, Then Click "Add Edges"', True, BLACK)
    screen.blit(instructTwoLabel_Surface, (50, 490))

def updateText(mode):
    global srcText_surface, srcText_rect
    global dstText_surface, dstText_rect
    global weightText_surface, weightText_rect
    
    if mode == 'clear' or mode == 'setSrc':
        # erase the previous value
        srcText_surface.fill(WHITE)
        screen.blit(srcText_surface, srcText_rect)

        # draw the new value
        srcText_surface = largeText.render("{:<8}".format('  ' + srcText), True, BLACK)
        srcText_rect = srcText_surface.get_rect()
        pygame.draw.rect(srcText_surface, BLACK, srcText_rect, 2)
        srcText_rect.topleft = (srcX, srcY+20)
        screen.blit(srcText_surface, srcText_rect)
               
    if mode == 'clear' or mode == 'setDst':
        dstText_surface.fill(WHITE)
        screen.blit(dstText_surface, dstText_rect)
                
        dstText_surface = largeText.render("{:<8}".format('  ' + dstText), True, BLACK)
        dstText_rect = dstText_surface.get_rect()
        pygame.draw.rect(dstText_surface, BLACK, dstText_rect, 2)
        dstText_rect.topleft = (dstX, dstY+20)
        screen.blit(dstText_surface, dstText_rect)
                
    if mode == 'clear' or mode == 'setWeight':
        weightText_surface.fill(WHITE)
        screen.blit(weightText_surface, weightText_rect)
                
        weightText_surface = largeText.render("{:<8}".format('  ' + weightText), True, BLACK)
        weightText_rect = weightText_surface.get_rect()
        pygame.draw.rect(weightText_surface, BLACK, weightText_rect, 2)
        weightText_rect.topleft = (weightX, weightY+20)
        screen.blit(weightText_surface, weightText_rect)
                
def getNode(nodeNum):
    for node in nodeList:
        if node.nodeNum == nodeNum:
            return node

def startGame():
    drawWeightInput()
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

            # when clicking on the srcNode input field
            elif srcText_rect.collidepoint(event.pos):
                mode = 'setSrc'
                srcText = ''

            # when clicking on the dstNode input field
            elif dstText_rect.collidepoint(event.pos):
                mode = 'setDst'
                dstText = ''

            # when clicking on the weight input field
            elif weightText_rect.collidepoint(event.pos):
                mode = 'setWeight'
                weightText = ''

            # when clicking on the 'Add Edge' button    
            elif addEdgeRect.collidepoint(event.pos):
                srcNodeNum = int(srcText)
                dstNodeNum = int(dstText)
                # for unweighted graph
                # when user does not set weight number
                # default weight to 0
                # do not draw 0 weight number on screen
                weightNum = int(weightText) if len(weightText)>0 else 0
                
                edgeSrcNode = getNode(srcNodeNum)
                edgeDstNode = getNode(dstNodeNum)
                newEdge = Edge(edgeSrcNode, edgeDstNode, weightNum)
                edgeList.append(newEdge)
                drawEdge(newEdge, BLACK, 2)
                # draw nodes on top of the edges
                drawNodes(nodeList)
                # set mode to clear
                mode = 'clear'

                srcText = ''
                dstText = ''
                weightText = '' 
                
                updateText(mode)
                #pygame.display.update()

        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                if mode == 'setSrc':
                    srcText = srcText[:-1]
                elif mode == 'setDst':
                    dstText = dstText[:-1]
                elif mode == 'setWeight':
                    weightText = weightText[:-1]
                
            else:
                if mode == 'setSrc':
                    srcText += event.unicode
                elif mode == 'setDst':
                    dstText += event.unicode
                elif mode == 'setWeight':
                    weightText += event.unicode

            updateText(mode)          

        # update the entire screen
        pygame.display.update()
                
pygame.quit()

    

