# Apple Pi Inc.
# Algorithmic Thinking
# Maze Solver with Depth-First Search Algorithm (DFS)
# Recursion Based Solution


# 2D array (i.e. list of list) to represent maze
def init_maze():
    maze = []
    maze.append(["#", " ", "O", "#"])
    maze.append(["#", " ", "#", " "])
    maze.append(["#", " ", " ", "#"])
    maze.append(["#", "#", "X", "#"])

    return maze

'''
def init_maze():
    maze = []
    maze.append(["#", "#", "#", "#", "#", "O", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", "#", "#", "#", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", " ", " ", " ", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#", "#"])
    maze.append(["#", " ", "#", " ", "#", " ", "#", "#", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#", "#"])
    maze.append(["#", "#", " ", "#", " ", "#", " ", " ", "#", "#"])
    maze.append(["#", " ", " ", " ", " ", " ", " ", " ", "#", "#"])
    maze.append(["#", "#", "X", "#", "#", "#", "#", "#", "#", "#"])

    return maze
'''

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
def print_maze(path=""):
    global maze
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
        


def valid(moves, visited):
    global maze
    coordinate = find_coordinate(moves)
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
def find_coordinate(moves):
    global maze
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

def find_end(moves):
    global maze, solutions
    coordinate =find_coordinate(moves)
    i = coordinate[0]
    j = coordinate[1]
    
    if (0 <= j < len(maze[0])) and (0 <= i < len(maze)) and (maze[i][j] == "X"):
        solutions.append(moves)
        print("Found: " + moves)
        print_maze(moves)
        return True
    return False


# Depth-First Search (DFS) Algorithm
maze = init_maze()
visited = init_visited()
solutions = []

# using DFS to find shortest path has to
# traverse through all possible paths and pick the
# shortest one
# the two parameters are used to maintain the local context (stack)
def solve_maze(moves, visited):
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
    
    solve_maze(moves + 'L', new_visited)
    solve_maze(moves + 'R', new_visited)    
    solve_maze(moves + 'U', new_visited)
    solve_maze(moves + 'D', new_visited)


solve_maze('', visited)
shortest_path = ''
minLength = 999999
print('-----------')
print('Total number of paths to exit: ' + str(len(solutions)))
for sol in solutions:
    if (len(sol) < minLength):
        minLength = len(sol)
        shortest_path = sol
print('Shortest ', end='')
print_maze(shortest_path)
