"""
class DirectedGraphNode:
     def __init__(self, x):
         self.label = x
         self.neighbors = []
"""
from collections import deque


class Solution:
    """
    @param graph: A list of Directed graph node
    @return: Any topological order for the given graph.
    """

    # get all in-degree
    def topSort(self, graph):
        # write your code here

        # get all indegree:
        def get_all_indegree(graph):
            node_to_degree = {x: 0 for x in graph}
            for node in graph:
                for neighbor in node.neighbors:
                    node_to_degree[neighbor] += 1
            return node_to_degree

        node_to_degree = get_all_indegree(graph)
        print('node_to_degree', node_to_degree)
        order = []
        queue = deque()
        for node in node_to_degree:
            if node_to_degree[node] == 0:
                queue.append(node)

        while queue:
            node = queue.popleft()
            # print(node.label)
            order.append(node)
            for neighbor in node.neighbors:
                node_to_degree[neighbor] -= 1
                if node_to_degree[neighbor] == 0:
                    queue.append(neighbor)
        return order