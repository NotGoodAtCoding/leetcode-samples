def longestCommonSubsequence(self, text1: str, text2: str) -> int:
    # cache in a 2d array where indexes refer to each of the
    # string indicies
    # iterate over each string and populate the cache:
    # if the chars match, increment both
    # else, split and increment one then the other

    sols = {}
    foundMax = 0
    for i1, c1 in enumerate(text1):
        for i2, c2 in enumerate(text2):
            if c1 == c2:
                sols[(i1,i2)] = sols.get((i1,i2), 0) + sols.get((i1-1, i2-1),0) +1
            else:
                sols[(i1,i2)] = max(sols.get((i1-1,i2), 0), sols.get((i1, i2-1), 0))
            foundMax = max(foundMax, sols[(i1,i2)])
    return foundMax

#         cache = [[0] * (len(text2)+1)] * (len(text1)+1)

#         for i in range(len(text1)-1, -1, -1):
#             for j in range(len(text2)-1, -1, -1):
#                 if text1[i] == text2[j]:
#                     cache[i][j] = 1 + cache[i+1][j+1]
#                 else:
#                     cache[i][j] = max(cache[i][j+1], cache[i+1][j])
#         return cache[0][0]
