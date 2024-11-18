def dfs_traversal(current_index, graph_matrix, visited_nodes, item_labels):
    
    print(item_labels[current_index], end=" ")
    
    visited_nodes[current_index] = 1

    for neighbor_index in range(len(graph_matrix)):
        if not visited_nodes[neighbor_index] and graph_matrix[current_index][neighbor_index] == 1:
            dfs_traversal(neighbor_index, graph_matrix, visited_nodes, item_labels)


def start_traversal():
    
    TOTAL_NODES = 9
    
    graph_matrix = [
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 1, 1, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 1], 
        [0, 0, 0, 0, 0, 0, 0, 0, 1],  
        [0, 0, 0, 1, 0, 0, 0, 0, 0], 
        [0, 0, 0, 0, 1, 0, 0, 1, 0],  
        [0, 0, 0, 0, 0, 0, 0, 1, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0],  
        [0, 0, 0, 0, 0, 0, 0, 0, 0]  
    ]

    visited_flags = [0] * TOTAL_NODES
  
    item_labels = ["watch", "shirt", "tie", "belt", "pants", "undershorts", "socks", "shoes", "jacket"]

    print("DFS traversal of the graph is: ", end="")
 
    for index in range(TOTAL_NODES):
        if not visited_flags[index]:
            dfs_traversal(index, graph_matrix, visited_flags, item_labels)

if __name__ == "__main__":
    start_traversal()
