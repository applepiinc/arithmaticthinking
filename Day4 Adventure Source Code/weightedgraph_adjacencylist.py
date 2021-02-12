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
        dstnode_weight = Node_Weight(dst_node, weight)
        self.adjlist[src_node].append(dstnode_weight)

    # Print the graph
    def print_graph(self):
      global adjlist
      for node in self.adjlist:
        for node_weight in self.adjlist[node]:
          print(node, " -> ", node_weight.node_num, " edge weight: ", node_weight.weight)

# demonstration graph
g = Graph(0)
# store the number of nodes in the graph
g.add_node(1)
g.add_node(2)
g.add_node(3)
g.add_node(4)
# add the edges between the nodes by specifying
# the src and dst nodes along with the edge weights
g.add_edge(1, 2, 1)
g.add_edge(1, 3, 1)
g.add_edge(2, 3, 3)
g.add_edge(3, 4, 4)
g.add_edge(4, 1, 5)
g.print_graph()

    
