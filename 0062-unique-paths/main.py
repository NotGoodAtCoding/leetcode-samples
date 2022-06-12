def uniquePaths(self, m: int, n: int) -> int:
    # could cache results in an mxn array of the ways to get to (m,n)
    # if a bottom or right edge, ans is always 1
    # else ans is the number below + number to the right
    # build the cache from bottom right to top left via adding
    # takes m*n operations

    nextRow = [1] * n

    for i in range(m-1):
        newRow = [1] * n
        for j in range(n-2, -1, -1):
            newRow[j] = newRow[j+1] + nextRow[j]
        nextRow = newRow
    return nextRow[0]


    # this may be able to be solved mathematically
    # m=1 -> 1
    # m=2 -> n
    # m=3 -> (m+1) * n
    # m=4 -> (m+1) * n

    # n=1 -> 1
    # n=2 -> m
    # n=3 -> (n+1) * m
