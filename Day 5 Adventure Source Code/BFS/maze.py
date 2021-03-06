# Apple Pi Inc.
# Algorithmic Thinking
# Maze

# 2D array (i.e. list of list) to represent maze
# 'O' marks start, 'X' marks end
def init_maze():
    maze = []
    maze.append(["#", " ", "O", "#"])
    maze.append(["#", " ", "#", " "])
    maze.append(["#", " ", " ", "#"])
    maze.append(["#", "#", "X", "#"])

    return maze

# nested for loop to
# traverse through 2D maze and print it
def print_maze(maze):

    for i, row in enumerate(maze):
        for j, col in enumerate(row):
            print(col + " ", end="")
        print()

maze = init_maze()
print_maze(maze)
