# Apple Pi Inc.
# Algorithmic Thinking
# Pygame Single Source Shortest Path With Dijkstra's Algorithm

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
YELLOW = (255,223,0)
RED = (182,0,37)

# set font size
large_text_size = 20
medium_text_size = 15

# initialize pygame
pygame.init()
# create a canvas for the desired dimension
screen = pygame.display.set_mode((WIDTH, HEIGHT))
screen.fill(WHITE)

pygame.display.set_caption("Python Dijkstra's Algorithm")
pygame.display.flip()
clock = pygame.time.Clock()

large_text = pygame.font.Font('freesansbold.ttf', large_text_size)
medium_text = pygame.font.Font('freesansbold.ttf', medium_text_size)

###### setup Graph variables ############

# variables for edge & weight input fields

# srcNode label coordinate
srcX, srcY = 50, 50
# dstNode label coordinate
dstX, dstY = 150, 50
# weight label coordinate
weightX, weightY = 250, 50
# 'Add Edge' label coordinate
addedgeX, addedgeY = 350, 50
# 'Find Shortest Path' label coordinate
shortestpathX, shortestpathY = 480, 50

# srcNode input box
src_text = ''
src_text_surface = large_text.render("{:<8}".format('  ' + src_text), True, BLACK)
src_text_rect = src_text_surface.get_rect()
pygame.draw.rect(src_text_surface, BLACK, src_text_rect, 2) 

# dstNode input box
dst_text = ''
dst_text_surface = large_text.render("{:<8}".format('  ' + dst_text), True, BLACK)
dst_text_rect = dst_text_surface.get_rect()
pygame.draw.rect(dst_text_surface, BLACK, dst_text_rect, 2) 

# weight input box
weight_text = ''
weight_text_surface = large_text.render("{:<8}".format('  ' + weight_text), True, BLACK)
weight_text_rect = weight_text_surface.get_rect()
pygame.draw.rect(weight_text_surface, BLACK, weight_text_rect, 2)

# set clickable text
addedge_surface = large_text.render("Add Edge", True, BLACK)
addedge_rect = addedge_surface.get_rect()

shortestpath_surface = large_text.render("Find Shortest Path", True, BLACK)
shortestpath_rect = shortestpath_surface.get_rect()

# initialize the input number
srcnode_num = -1
dstnode_num = -1
weight_num = -1

# variables for node
node_num = 1
nodelist = []
edgelist = []
node_radius = 16

# mode represents which field is being modified by user
# 'setSrc', 'setDst', 'setWeight', 'clear'
mode = ''

class Node:
    # instance variables
    x: int
    y: int
    node_num: int

    # constructor
    # a. called when creating an object of type Node
    # b. purpose is to initialize instance variables
    # c. always named __init__
    # d. first parameter 'self' allows accessing the instance variables
    def __init__(self, x: int, y: int, node_num: int):
        # use keyword 'self' to refer to instance variables
        self.x = x
        self.y = y
        self.node_num = node_num

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

class Node_Weight:
    
    def __init__(self, node_num, weight) :
        self.node_num = node_num
        self.weight = weight

class Graph:
    
    def __init__(self, node_count) :
        self.adjlist = {}
        self.node_count = node_count

    def add_node(self, node):
      global adjlist
      global node_count
      if node in self.adjlist:
        print("node ", node, " already exists.")
      else:
        self.node_count = self.node_count + 1
        self.adjlist[node] = []

    # add an edge between src_node and dst_node with edge weight
    def add_edge(self, src_node, dst_node, weight):
      global adjlist
      # check if node src_node is a valid node
      if src_node not in self.adjlist:
        print("node ", src_node, " does not exist.")
      # check if node dst_node is a valid node
      elif dst_node not in self.adjlist:
        print("node ", dst_node, " does not exist.")
      else:
        # for undirected graph,
        # add both src -> dst and dst -> src
        dstnode_weight = Node_Weight(dst_node, weight)
        self.adjlist[src_node].append(dstnode_weight)

        srcnode_weight = Node_Weight(src_node, weight)
        self.adjlist[dst_node].append(srcnode_weight)


    # Print the graph
    def print_graph(self):
      global adjlist
      for node in self.adjlist:
        for node_weight in self.adjlist[node]:
          print(node, " -> ", node_weight.node_num, " edge weight: ", node_weight.weight)

    def dijkstra_shortest_path(self, source) :

        # Initialize the distance of all the nodes from source to infinity
        distance = [999999999999] * (self.node_count + 1)
        # Distance of source node to itself is 0
        distance[source] = 0

        # create a dictionary to keep track how far
        # nodes are from the starting point
        # {node, distance_from_source }
        dict_node_length = {source: 0}

        while dict_node_length :

            # select the node with the shortest distance from the source
            # (get the key for the smallest value in the dictionary)
            srcnode = min(dict_node_length, key = lambda k: dict_node_length[k])
            # remove the processed node so we will not check it again
            del dict_node_length[srcnode]

            # orient on current src node and
            # update the distances to its directly reachable nodes
            for dstnode_weight in self.adjlist[srcnode] :
                adjnode = dstnode_weight.node_num
                weight_to_adjnode = dstnode_weight.weight

                # edge relaxation
                # update the distances to its directly reachable locations
                if distance[adjnode] > distance[srcnode] + weight_to_adjnode :
                    distance[adjnode] = distance[srcnode] + weight_to_adjnode
                    dict_node_length[adjnode] = distance[adjnode]

        n = 0
        for i in range(1, self.node_count+1) :
            # draw shortest path on screen
            distance_surface = large_text.render(str(source) + " -> " + str(i) + ": " + str(distance[i]), True, RED)
            screen.blit(distance_surface, (shortestpathX + 300, shortestpathY + n))
            n += 20
            print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))

def draw_node(node):
    # draw node circle centered at (node.x, node.y)
    pygame.draw.circle(screen, LIGHT_BROWN, (node.x, node.y), node_radius)

    # draw the node number
    nodeSurface = large_text.render(str(node.node_num), True, WHITE)
    # define the rect value of the nodeSurface centered in the circle
    nodeRect = nodeSurface.get_rect(center=(node.x, node.y))
    # draw the node number on the screen at the rect position      
    screen.blit(nodeSurface, nodeRect)

def draw_nodes(nodes):
    for node in nodes:
        draw_node(node)
    
def draw_edge(edge, color, edge_width):
    edgesrcX, edgesrcY = edge.src.x, edge.src.y
    edgedstX, edgedstY = edge.dst.x, edge.dst.y
    weight = edge.weight
    pygame.draw.line(screen, color, (edgesrcX, edgesrcY), (edgedstX, edgedstY), width=edge_width)
    # only draw weight number when not zero
    if weight !=0:
        weight_label_surface = large_text.render(str(weight), True, color)
        weightlabelX = int((edgesrcX + edgedstX)/2)
        weightlabelY = int((edgesrcY + edgedstY)/2)

        # when edge is tilted from topleft to bottomright
        # make sure weight number not overlapping with edge line
        if ((edgesrcX-edgedstX) * (edgesrcY-edgedstY) > 0):
            weightlabelX -= 9
        else:
            weightlabelX += 3
            weightlabelY += 3
        screen.blit(weight_label_surface, (weightlabelX, weightlabelY))

def draw_edges(edges, color, edge_width):
    for edge in edges:
        draw_edge(edge, color, edge_width)
        
def draw_weight_input():
    src_label_surface = medium_text.render("Src Node #", True, BLACK)
    screen.blit(src_label_surface, (srcX, srcY))
    src_text_rect.topleft = (srcX, srcY+20)
    screen.blit(src_text_surface, src_text_rect)
    
    dst_label_surface = medium_text.render("Dst Node #", True, BLACK)
    screen.blit(dst_label_surface, (dstX, dstY))
    dst_text_rect.topleft = (dstX, dstY+20)
    screen.blit(dst_text_surface, dst_text_rect)

    weight_label_surface = medium_text.render("Weight", True, BLACK)
    screen.blit(weight_label_surface, (weightX, weightY))
    weight_text_rect.topleft = (weightX, weightY+20)
    screen.blit(weight_text_surface, weight_text_rect)

    addedge_rect.topleft = (addedgeX, addedgeY)
    screen.blit(addedge_surface, addedge_rect)

    shortestpath_rect.topleft = (shortestpathX, shortestpathY)
    screen.blit(shortestpath_surface, shortestpath_rect)
   

def draw_instruction():
    # box dimension: topleft (50, 110), bottomright (750, 440)
    pygame.draw.rect(screen, BROWN, pygame.Rect(50, 110, 700, 330), 2)
    instructone_label_surface = medium_text.render('Step 1: Click Inside Box to Add Nodes', True, BLACK)
    screen.blit(instructone_label_surface, (50, 460))

    instructtwo_label_surface = medium_text.render('Step 2: Enter Src Node #, Dst Node # and Weight, Then Click "Add Edges"', True, BLACK)
    screen.blit(instructtwo_label_surface, (50, 490))

    instructthree_label_surface = medium_text.render('Step 3: Click "Find Shortest Path"', True, BLACK)
    screen.blit(instructthree_label_surface, (50, 520))

def update_text(mode):
    global src_text_surface, src_text_rect
    global dst_text_surface, dst_text_rect
    global weight_text_surface, weight_text_rect
    
    if mode == 'clear' or mode == 'setSrc':
        # erase the previous value
        src_text_surface.fill(WHITE)
        screen.blit(src_text_surface, src_text_rect)

        # draw the new value
        src_text_surface = large_text.render("{:<8}".format('  ' + src_text), True, BLACK)
        src_text_rect = src_text_surface.get_rect()
        pygame.draw.rect(src_text_surface, BLACK, src_text_rect, 2)
        src_text_rect.topleft = (srcX, srcY+20)
        screen.blit(src_text_surface, src_text_rect)
               
    if mode == 'clear' or mode == 'setDst':
        dst_text_surface.fill(WHITE)
        screen.blit(dst_text_surface, dst_text_rect)
                
        dst_text_surface = large_text.render("{:<8}".format('  ' + dst_text), True, BLACK)
        dst_text_rect = dst_text_surface.get_rect()
        pygame.draw.rect(dst_text_surface, BLACK, dst_text_rect, 2)
        dst_text_rect.topleft = (dstX, dstY+20)
        screen.blit(dst_text_surface, dst_text_rect)
                
    if mode == 'clear' or mode == 'setWeight':
        weight_text_surface.fill(WHITE)
        screen.blit(weight_text_surface, weight_text_rect)
                
        weight_text_surface = large_text.render("{:<8}".format('  ' + weight_text), True, BLACK)
        weight_text_rect = weight_text_surface.get_rect()
        pygame.draw.rect(weight_text_surface, BLACK, weight_text_rect, 2)
        weight_text_rect.topleft = (weightX, weightY+20)
        screen.blit(weight_text_surface, weight_text_rect)
                
def getNode(node_num):
    for node in nodelist:
        if node.node_num == node_num:
            return node

def startGame():
    draw_weight_input()
    draw_instruction()
    pygame.display.update()

# pygame loop to continuously take user input
running = True
g = Graph(0)

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
            if (mouse_x > 50+node_radius and mouse_x < 750-node_radius) \
                and (mouse_y > 110+node_radius and mouse_y <440-node_radius):
                # add new node to the list
                nodelist.append(Node(mouse_x, mouse_y, node_num))

                # add new node to the graph
                g.add_node(node_num)
                
                # draw new node
                # using list here for graph processing in the next step
                draw_node(Node(mouse_x, mouse_y, node_num))

                # increase node number by 1
                node_num += 1

            # when clicking on the srcNode input field
            elif src_text_rect.collidepoint(event.pos):
                mode = 'setSrc'
                src_text = ''

            # when clicking on the dstNode input field
            elif dst_text_rect.collidepoint(event.pos):
                mode = 'setDst'
                dst_text = ''

            # when clicking on the weight input field
            elif weight_text_rect.collidepoint(event.pos):
                mode = 'setWeight'
                weight_text = ''

            # when clicking on the 'Add Edge' button    
            elif addedge_rect.collidepoint(event.pos):
                srcnode_num = int(src_text)
                dstnode_num = int(dst_text)
                # for unweighted graph
                # when user does not set weight number
                # default weight to 0
                # do not draw 0 weight number on screen
                weight_num = int(weight_text) if len(weight_text)>0 else 0

                # add edge to the graph
                g.add_edge(srcnode_num, dstnode_num, weight_num)
                
                edge_srcnode = getNode(srcnode_num)
                edge_dstnode = getNode(dstnode_num)
                newedge = Edge(edge_srcnode, edge_dstnode, weight_num)
                edgelist.append(newedge)
                draw_edge(newedge, BLACK, 2)
                # draw nodes on top of the edges
                draw_nodes(nodelist)
                # set mode to clear
                mode = 'clear'

                src_text = ''
                dst_text = ''
                weight_text = '' 
                
                update_text(mode)

            elif shortestpath_rect.collidepoint(event.pos):
                g.print_graph()
                g.dijkstra_shortest_path(1)


        elif event.type == pygame.KEYDOWN:

            if event.key == pygame.K_BACKSPACE:
                if mode == 'setSrc':
                    src_text = src_text[:-1]
                elif mode == 'setDst':
                    dst_text = dst_text[:-1]
                elif mode == 'setWeight':
                    weight_text = weight_text[:-1]
                
            else:
                if mode == 'setSrc':
                    src_text += event.unicode
                elif mode == 'setDst':
                    dst_text += event.unicode
                elif mode == 'setWeight':
                    weight_text += event.unicode

            update_text(mode)          

        # update the entire screen
        pygame.display.update()
                
pygame.quit()

    

