class BreadthFirstSearch:
    # For breadth first search we are passing the graph,
    # the node from which the graph is traversed and the node you want to find as arguments
    def bfsearch(self, graph, node, s_element):
        # In BFS we traverse the graph based on the level.
        # So, we use queues to perform FIFO (First In First Out)
        # an empty list to store the nodes visited to overcome cycles in graph
        visited = []
        queue = []
        if node not in visited:
            visited.append(node)
            queue.append(node)
        # This method returns 0 or 1 based on the search element
        found = 0
        while queue:
            # Every time an element is popped, it is considered as current element
            element = queue.pop(0)
            # We check if the current element has any neighbours
            # If the neighbours of the current element are not visited we add them to visited list and the queue
            for neighbour in graph[element]:
                if neighbour not in visited:
                    visited.append(neighbour)
                    queue.append(neighbour)
                if s_element in visited:
                    found = 1
                    # We use break to stop moving further when the search element is found
                    break
                else:
                    found = 0
        return found


# If you want to use the above class from the same file, uncomment the code below and run
"""b = BreadthFirstSearch()
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
print(b.bfsearch(graph, 'A', 'K'))"""
