def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
    # for each cell on the border of each ocean,
    # traverse the graph using dfs in cardinal directions as long as it is mono increasing
    # add the visited coords to a set of valid coords for each ocean

    rows, cols = len(heights), len(heights[0])

    processed_atl, processed_pac = set(), set()

    def dfs(x, y, processed, prevHeight):
        if ((x,y) in processed
            or x == rows or y == cols
            or x < 0 or y < 0
            or heights[x][y] < prevHeight):
            return
        processed.add((x,y))

        dfs(x+1, y, processed, heights[x][y])
        dfs(x-1, y, processed, heights[x][y])
        dfs(x, y-1, processed, heights[x][y])
        dfs(x, y+1, processed, heights[x][y])

    # perform on north/south coast
    for c in range(cols):
        dfs(0, c, processed_pac, heights[0][c])  #north
        dfs(rows-1, c, processed_atl, heights[rows-1][c])  #south

    # perform on east/west coast
    for r in range(rows):
        dfs(r, 0, processed_pac, heights[r][0]) #west
        dfs(r, cols-1, processed_atl, heights[r][cols-1])  #east

    ans = []
    for r in range(rows):
        for c in range(cols):
            if (r,c) in processed_pac and (r,c) in processed_atl:
                ans.append([r,c])  #construct answer

    return ans
