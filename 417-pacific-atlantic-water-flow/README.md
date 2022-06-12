Bit of a messy implementation.

For each coast, we iterate over the coastal grid blocks, perform a DFS to mark all grid points that are of a monotonically increasing height as draining to the given ocean.

We must then construct the answer, which is fairly inefficient. 
