# graphs_delagarza

A specialized Python graph algorithm library packaging assignment for MSU Denver. This Package implements pathfinding and traversal utilities, structured to be natively installable via pip.

## Features

- **Dijkstra's Algorithm**: Calculates the absolute shortest paths from a single source node to all other reachable nodes in a weighted network graph, representing disconnected paths utilizing a standard maxsize boundary.
- **Breadth-First Search (BFS)**: Traverses a structural network layer by layer to catalog reachable nodes in their exact order of discovery.

## Installation

```bash
pip install graphs_delagarza
```

### For development

Ensure your local virtual environment is activated, then execute an editable local installation from the project root directory:

Clone the repo, then from the project root:

```bash
pip install -e .
```


## Usage

```python
from graphs_delagarza import dijkstra, bfs

# Define a standard network graph structure
graph = {
    'A': {'B': 1, 'C': 4},
    'B': {'C': 2, 'D': 5},
    'C': {'D': 1},
    'D': {}
}

# 1. Execute Shortest Path Routing
dist, path = dijkstra(graph, 'A')
print("Dijkstra Distances:", dist)
print("Dijkstra Paths:", path)

# 2. Execute Graph Node Traversal
visited_order = bfs(graph, 'A')
print("BFS Visited Order:", visited_order)
```

## Repo Link
URL for your GitHub repository: https://github.com/jdelagar/26FCS3250-002-hwk-5
