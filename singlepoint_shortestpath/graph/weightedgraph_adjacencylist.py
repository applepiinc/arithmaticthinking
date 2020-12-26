# Apple Pi Inc.
# Algorithmic Thinking
# Weighted Graph Using Adjacency List

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

    # Add an edge between node node1 and node2 with edge weight e
    def add_edge(self, node1, node2, e):
      global adjlist
      # Check if node node1 is a valid node
      if node1 not in self.adjlist:
        print("node ", node1, " does not exist.")
      # Check if node node2 is a valid node
      elif node2 not in self.adjlist:
        print("node ", node2, " does not exist.")
      else:
        # Since this code is not restricted to a directed or 
        # an undirected graph, an edge between node1 node2 does not
        # imply that an edge exists between node2 and node1
        temp = Node_Weight(node2, e)
        self.adjlist[node1].append(temp)

    # Print the graph
    def print_graph(self):
      global adjlist
      for node in self.adjlist:
        for node_weight in self.adjlist[node]:
          print(node, " -> ", node_weight.node_num, " edge weight: ", node_weight.weight)

# demonstration graph
g = Graph(0)
# stores the number of nodes in the graph
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
# Add the edges between the nodes by specifying
# the from and to nodes along with the edge weights.
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 3)
g.add_edge(3, 4, 4)
g.add_edge(4, 1, 5)
g.print_graph()

    
