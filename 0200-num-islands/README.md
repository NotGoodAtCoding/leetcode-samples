The core of the algorithm is fairly simple: Check all points on the grid, once LAND is found that has NOT been visited, perform a BFS to mark all connected lands as "visited" and increment the number of islands.

Implemented with BFS, seems like DFS implementations tend to perform better for this problem. 
