import sys
from heapq import heappush, heappop

def dijkstra(graph, source):
    dist = {node: sys.maxsize for node in graph}
    dist[source] = 0
    heap = []
    heappush(heap, (0, source))
    path = {source: []}

    while heap:
        w, u = heappop(heap)
        for v in graph.get(u, {}):
            if w + graph[u][v] < dist[v]:
                dist[v] = w + graph[u][v]
                heappush(heap, (dist[v], v))
                path[v] = path[u] + [u]

    return dist, path

from collections import deque

def bfs(graph, start):
    """
    Traverses the graph using Breadth-First Search.
    Returns a list of nodes in the order they were visited.
    """
    visited = []
    queue = deque([start])

    while queue:
        vertex = queue.popleft()
        if vertex not in visited:
            visited.append(vertex)
            if vertex in graph:
                for neighbor in graph[vertex]:
                    if neighbor not in visited:
                        queue.append(neighbor)
    return visited