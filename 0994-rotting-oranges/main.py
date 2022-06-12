def orangesRotting(self, grid: List[List[int]]) -> int:
    # implement a BFS
    # initialize with the coords of the initial rotten oranges
    # add surrounding fresh oranges to the queue

    que = collections.deque()
    curTime, fresh = 0, 0

    rows, cols = len(grid), len(grid[0])

    for r in range(rows):
        for c in range(cols):
            if grid[r][c] == 1:
                fresh += 1 # count how many are fresh
            elif grid[r][c] == 2:
                que.append((r,c))  #add rotten to queue

    DIRS = [[1,0], [-1,0], [0,1], [0,-1]]
    while que and fresh > 0:

        for i in range(len(que)):
            r, c = que.popleft()

            for dr, dc in DIRS:
                row, col = r+dr, c+dc

                if (row < 0 or row == rows
                   or col < 0 or col == cols
                   or grid[row][col] != 1):
                    continue
                grid[row][col] = 2
                que.append((row, col))
                fresh -=1

        curTime += 1
    return curTime if fresh == 0 else -1
