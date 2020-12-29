# Apple Pi Inc.
# Algorithmic Thinking
# Maze Solver with Breadth-First Search Algorithm (BFS)

import queue


# 2D array (i.e. list of list) to represent maze
def init_maze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", "#", "#", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#", "#"])
    maze.append(["#", "#", "#", "#", " ", "#", " ", " ", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#", "#"])
    maze.append(["#", "#", "X", "#", "#", "#", "#", "#", "#", "#"])

    return maze

# performance optimization
# 2D array (list of list) to keep track of the visited locations
# so that we do not revisit them
def init_visited():
    visited = []
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
    visited.append([0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    return visited

# traverse through 2D maze and
# print it along with the solution path
def print_maze(maze, path=""):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    j = start
    i = 0
    
    # pos stores the locations
    # along the solution path
    pos = set()
    print("Path moves: ", end="")
    for move in path:
        if move == "L":
            j -= 1

        elif move == "R":
            j += 1

        elif move == "U":
            i -= 1

        elif move == "D":
            i += 1
        print((i, j), end = ':')
        pos.add((i, j))
    print()
    
    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            if (i, j) in pos:
                print("+ ", end="")
            else:
                print(col + " ", end="")
        print()
        


def valid(maze, moves):
    coordinate = find_coordinate(maze, moves)
    i = coordinate[0]
    j = coordinate[1]
    
    # if outside of boundary
    if not(0 <= j < len(maze[0]) and 0 <= i < len(maze)):
        return False
    
    # if road block
    elif (maze[i][j] == "#"):
        return False
    
    # if visited
    elif (visited[i][j] == 1):
        return False

    return True


# convert location steps ((e.g.DLLDR) to row/column indexes
def find_coordinate(maze, moves):
    for x, pos in enumerate(maze[0]):
        if pos == "O":
            start = x

    j = start
    i = 0
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

def find_end(maze, moves):
    coordinate =find_coordinate(maze, moves)
    i = coordinate[0]
    j = coordinate[1]
    
    if (0 <= j < len(maze[0])) and (0 <= i < len(maze)) and (maze[i][j] == "X"):
        print("Found: " + moves)
        print_maze(maze, moves)
        return True

    return False



# Breadth-First Search (BFS) Algorithm
maze = init_maze()
visited = init_visited()

# queue keeps track of the unvisited locations
# location is represented by the steps to
# move there from the starting point (e.g.DLLDR) 
loc_queue = queue.Queue()
loc_queue.put("")
moves = ""

run = True
while run: 
    moves = loc_queue.get()
    # explore surrounding neighbours (breadth)
    # left, right, up, down
    for neighbour in ["L", "R", "U", "D"]:
        new_moves = moves + neighbour
        
        if find_end(maze, new_moves):
            run = False
            break
            
        elif valid(maze, new_moves):
            loc_queue.put(new_moves)
            coordinate = find_coordinate(maze, new_moves)
            i = coordinate[0]
            j = coordinate[1]
            visited[i][j] = 1   
            
