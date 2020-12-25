# Apple Pi Inc.
# Algorithmic Thinking
# MST Kruskal's Algorithm

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
    parent: list
    mst: list
    
    # constructor
    def __init__(self, nodeList: int, edgeList: list):
        self.nodeList = nodeList
        self.edgeList = edgeList
        self.parent = [None]*(len(self.nodeList)+1)
        self.mst = []

     # recursion method to find root node of the tree
    def findRoot(self, node):
        # base case: when the parent node is itself
        if self.parent[node] == node:
            return node
        
        # otherwise, recursively call current method to
        # traverse up the parent node
        return self.findRoot(self.parent[node])

    # Kruskal's Algorithm
    def kruskalMST(self):
        # sort edges based on weight
        # "key" specifies the sorting criteria
        # "lambda" creates an anonymous function that
        # returns weight of the edge
        # in this case, it sorts by weight of the edge
        self.edgeList.sort(key=lambda Edge: Edge.weight)

        # At the beginning, each node itself is a tree
        # initialize parent list
        for n in range(len(self.nodeList)+1):
            # to start, every node is the parent of itself
            self.parent[n] = n
   
        # loop through each edge in sorted order
        # if the src and dst nodes
        # are from different trees (different root nodes), it means that
        # adding this edge will not form a cycle,
        # then add the edge to MST and merge trees
        for edge in self.edgeList:
            
            srcTreeRoot = self.findRoot(edge.src.nodeNum)
            dstTreeRoot = self.findRoot(edge.dst.nodeNum)

            # if no cycle formed
            # then add the edge to MST and merge trees
            if srcTreeRoot != dstTreeRoot:
                
                self.mst.append(edge)
                # merge the trees
                self.parent[dstTreeRoot] = srcTreeRoot
                    
        print("MST in this graph [<Connection>: <Weight>]: ")
        cost = 0
        for edge in self.mst:
            print("[" + str(edge.src.nodeNum) + "-" + str(edge.dst.nodeNum) + ": " +
                  str(edge.weight) + "]", end = " ")
            cost += edge.weight
        print("\nCost of MST: " + str(cost))

# demonstration nodes and edges
nodeList = [Node(245, 164, 1), Node(155, 255, 2), Node(245, 345, 3), Node(335, 255, 4), Node(515, 255, 5)]
edgeList = [Edge(Node(245, 164, 1), Node(155, 255, 2), 3),
            Edge(Node(245, 164, 1), Node(335, 255, 4), 1),
            Edge(Node(155, 255, 2), Node(245, 345, 3), 5),
            Edge(Node(245, 345, 3), Node(335, 255, 4), 7),
            Edge(Node(335, 255, 4), Node(515, 255, 5), 6)]
g1 = Graph(nodeList, edgeList)
g1.kruskalMST()
