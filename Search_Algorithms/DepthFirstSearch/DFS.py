class DepthFirstSearch:
    # For depth first search we are passing the graph, an empty list to store the visited nodes,
    # the node from which the graph is traversed and the node you want to find as arguments
    def dfsearch(self, graph, visited, node, s_element):
        # In DFS we traverse the graph based on the depth in the graph.
        # So, we use queues to perform LIFO (Last In First Out)
        # the visited list is used to store the nodes visited to overcome cycles in graph
        if node not in visited:
            visited.append(node)
            # If the neighbours of the current element are not visited we add them to visited list
            for neighbour in graph[node]:
                self.dfsearch(graph, visited, neighbour, s_element)
        if s_element in visited:
            found1 = 1
        else:
            found1 = 0
        # This method returns 0 or 1 based on the search element
        return found1


# If you want to use the above class from the same file, uncomment the code below and run
"""d = DepthFirstSearch()
graph = {
    'A': ['B', 'C'],
    'B': ['D', 'E'],
    'C': ['F'],
    'D': [],
    'E': ['F'],
    'F': []
}
visited = []
print(d.dfsearch(graph, visited, 'A', 'C'))"""
