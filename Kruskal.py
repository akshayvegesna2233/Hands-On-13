MAX_VERTICES = 30

class GraphEdge:
    def __init__(self, start, end, weight):
        self.start = start  
        self.end = end  
        self.weight = weight 

class EdgeCollection:
    def __init__(self):
        self.edges = []  
        self.edge_count = 0  

graph_matrix = [
    [0, 4, 0, 0, 0, 0, 0, 8, 0],
    [4, 0, 8, 0, 0, 0, 0, 11, 0],
    [0, 8, 0, 7, 0, 4, 0, 0, 2],
    [0, 0, 7, 0, 9, 14, 0, 0, 0],
    [0, 0, 0, 9, 0, 10, 0, 0, 0],
    [0, 0, 4, 14, 10, 0, 2, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 1, 6],
    [8, 0, 0, 0, 0, 0, 1, 0, 7],
    [0, 0, 2, 0, 0, 0, 6, 7, 0]
]

total_nodes = 9

parent_node = [i for i in range(MAX_VERTICES)]

node_labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i']

edge_list = EdgeCollection()

def minimum_spanning_tree():
    global edge_list
    edge_list.edge_count = 0

    for row in range(total_nodes):
        for col in range(total_nodes):
            if graph_matrix[row][col] != 0:
                edge_list.edges.append(GraphEdge(row, col, graph_matrix[row][col]))
                edge_list.edge_count += 1

    edge_list.edges.sort(key=lambda edge: edge.weight)
    print("\nEdges of the Minimum Cost Spanning Tree are:")
    for edge in edge_list.edges:
        src_root = get_root(edge.start)
        dest_root = get_root(edge.end)

        if src_root != dest_root:
            connect_nodes(src_root, dest_root)
            print(f"{node_labels[edge.start]} -> {node_labels[edge.end]} = {edge.weight}")

def get_root(node):
    while parent_node[node] != node:
        node = parent_node[node]
    return node

def connect_nodes(node1, node2):
    parent_node[node1] = node2

if __name__ == "__main__":
    minimum_spanning_tree()
