def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
    rows, cols = len(grid), len(grid[0])
    counted = set()  # set of tuple coordinates of visited land mass

    max_area = 0

    def dfs(x,y):
        if (x<0 or x == rows or y < 0 or y == cols or grid[x][y] ==0 or (x,y) in counted):
            return 0
        counted.add((x,y))
        return (1
                + dfs(x+1, y)
                + dfs(x-1, y)
                + dfs(x, y+1)
                + dfs(x, y-1)
               )
    for r in range(rows):
        for c in range(cols):
            max_area = max(max_area, dfs(r,c))
    return max_area
