import heapq

def prim(graph):
    # Start with any vertex
    start = list(graph.keys())[0]

    # Track vertices that are included in the MST
    visited = set()

    # Track edges in the MST
    mst = []

    # weight, vertex u, vertex v
    min_heap = [(0, start, None)]

    while min_heap:
        weight, current, prev = heapq.heappop(min_heap)  # O(log E)

        if current in visited:
            continue

        visited.add(current) # O(1)

        if prev is not None:
            mst.append((prev, current, weight)) # O(1)

        for neighbor, edge_weight in graph[current].items(): # O(E)
            if neighbor not in visited:
                heapq.heappush(min_heap, (edge_weight, neighbor, current))

    return mst


graph = {
    'A': { 'B': 4, 'E': 4 },
    'B': { 'A': 4, 'C': 1, 'G': 6, 'D': 8 },
    'C': { 'B': 1, 'E': 5 },
    'D': { 'B': 8, 'F': 7, 'H': 3 },
    'E': { 'A': 4, 'C': 5 },
    'F': { 'D': 7 },
    'G': { 'B': 6, 'H': 5 },
    'H': { 'D': 3, 'G': 5 },
}

mst = prim(graph)

print("Edges in the Minimum Spanning Tree:")
total_weight = 0
for u, v, weight in mst:
    print(f"Edge ({u}, {v}) with weight {weight}")
    total_weight += weight

print(f"Total weight of MST: {total_weight}")
