# Algorithms and Data Structures - Prim


## Characteristics
- Time complexity: O(E log V) where E is the number of edges and V is the number of vertices.
  - Because Prim's algorithm uses a priority queue to select the minimum weight edge, which takes O(log V) time for each edge.
- Space complexity: O(V + E) for storing the graph and the MST.



## Demos

```mermaid
graph LR
  A((A)) -- 4 --- B((B))
  A -- 4 --- E((E))
  B -- 1 --- C((C))
  B -- 6 --- G((G))
  B -- 8 --- D((D))
  C -- 5 --- E
  D -- 7 --- F((F))
  D -- 3 --- H((H))
  H -- 5 --- G
```

[Implementation](./src/prim.py)



## References
- [Other Algorithms & Data Structures](https://github.com/NelsonBN/algorithms-data-structures)
