# Apple Pi Inc.
# Algorithmic Thinking
# Single Point Shortest Path With Dijkstra's Algorithm

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

    def dijkstra_shortest_path(self, source) :

        # Initialize the distance of all the nodes from source to infinity
        distance = [999999999999] * (self.node_count + 1)
        # Distance of source node to itself is 0
        distance[source] = 0

        # Create a dictionary of { node, distance_from_source }
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

        for i in range(1, self.node_count+1) :
            print("Source Node ("+str(source)+")  -> Destination Node(" + str(i) + ")  : " + str(distance[i]))


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

g.dijkstra_shortest_path(1)
   
