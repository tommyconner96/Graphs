"""
Simple graph implementation
"""
from util import Stack, Queue  # These may come in handy
import copy

class Graph:

    """Represent a graph as a dictionary of vertices mapping labels to edges."""
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, vertex_id):
        self.vertices[vertex_id] = set()

    def add_edge(self, v1, v2):
        # paramaters are v1, and v2 with v2 being added
        # to v1
        if v1 in self.vertices and v2 in self.vertices:
            self.vertices[v1].add(v2)
        else:
            print("error: vertex not found")

    def get_neighbors(self, vertex_id):
        return self.vertices[vertex_id]
    # test not passsing
    def bft(self, starting_vertex):
        queue = []
        queue.append(starting_vertex)

        visited = set()
        while len(queue) > 0:
            current_vertex = queue.pop(0)

            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    queue.append(neighbor)
                    # print(neighbor)
        
# test not passing
    def dft(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.
        """
        stack = []
        stack.append(starting_vertex)

        visited = set()

        while len(stack) > 0:
            current_vertex = stack.pop()
            if current_vertex not in visited:
                print(current_vertex)
                visited.add(current_vertex)

                for neighbor in self.get_neighbors(current_vertex):
                    stack.append(neighbor) 

    def dft_recursive(self, starting_vertex):
        """
        Print each vertex in depth-first order
        beginning from starting_vertex.

        This should be done using recursion.
        """
        pass  # TODO
# working
    def bfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing the shortest path from
        starting_vertex to destination_vertex in
        breath-first order.
        """
        queue = [[starting_vertex]]

        visited = set()

        while len(queue) > 0:
            current_path = queue.pop(0)

            current_vertex = current_path[-1]

            if current_vertex not in visited:

                visited.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path
                
                for neighbor in self.get_neighbors(current_vertex):
                    current_path_copy = list(current_path)

                    current_path_copy.append(neighbor)

                    queue.append(current_path_copy)
        return None

# working
    def dfs(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.
        """
        stack = [[starting_vertex]]

        visited = set()

        while len(stack) > 0:
            current_path = stack.pop()

            current_vertex = current_path[-1]

            if current_vertex not in visited:

                visited.add(current_vertex)

                if current_vertex == destination_vertex:
                    return current_path
                
                for neighbor in self.get_neighbors(current_vertex):
                    current_path_copy = list(current_path)

                    current_path_copy.append(neighbor)

                    stack.append(current_path_copy)
        return None

    def dfs_recursive(self, starting_vertex, destination_vertex):
        """
        Return a list containing a path from
        starting_vertex to destination_vertex in
        depth-first order.

        This should be done using recursion.
        """
        pass  # TODO

if __name__ == '__main__':
    graph = Graph()  # Instantiate your graph
    # https://github.com/LambdaSchool/Graphs/blob/master/objectives/breadth-first-search/img/bfs-visit-order.png
    graph.add_vertex(1)
    graph.add_vertex(2)
    graph.add_vertex(3)
    graph.add_vertex(4)
    graph.add_vertex(5)
    graph.add_vertex(6)
    graph.add_vertex(7)
    graph.add_edge(5, 3)
    graph.add_edge(6, 3)
    graph.add_edge(7, 1)
    graph.add_edge(4, 7)
    graph.add_edge(1, 2)
    graph.add_edge(7, 6)
    graph.add_edge(2, 4)
    graph.add_edge(3, 5)
    graph.add_edge(2, 3)
    graph.add_edge(4, 6)

    '''
    Should print:
        {1: {2}, 2: {3, 4}, 3: {5}, 4: {6, 7}, 5: {3}, 6: {3}, 7: {1, 6}}
    '''
    print(graph.vertices)

    '''
    Valid BFT paths:
        1, 2, 3, 4, 5, 6, 7
        1, 2, 3, 4, 5, 7, 6
        1, 2, 3, 4, 6, 7, 5
        1, 2, 3, 4, 6, 5, 7
        1, 2, 3, 4, 7, 6, 5
        1, 2, 3, 4, 7, 5, 6
        1, 2, 4, 3, 5, 6, 7
        1, 2, 4, 3, 5, 7, 6
        1, 2, 4, 3, 6, 7, 5
        1, 2, 4, 3, 6, 5, 7
        1, 2, 4, 3, 7, 6, 5
        1, 2, 4, 3, 7, 5, 6
    '''
    graph.bft(1)
    # print(graph.bft(1))

    '''
    Valid DFT paths:
        1, 2, 3, 5, 4, 6, 7
        1, 2, 3, 5, 4, 7, 6
        1, 2, 4, 7, 6, 3, 5
        1, 2, 4, 6, 3, 5, 7
    '''
    graph.dft(1)
    print(graph.dft(1))
    graph.dft_recursive(1)

    '''
    Valid BFS path:
        [1, 2, 4, 6]
    '''
    print(graph.bfs(1, 6))

    '''
    Valid DFS paths:
        [1, 2, 4, 6]
        [1, 2, 4, 7, 6]
    '''
    print(graph.dfs(1, 6))
    # print(graph.dfs_recursive(1, 6))
    