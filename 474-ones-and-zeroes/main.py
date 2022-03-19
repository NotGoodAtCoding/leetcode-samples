
# Deprecated - non-optimal solution

# def findMaxForm(self, strs: List[str], m: int, n: int) -> int:
#
#     paths = {(0,0): 0}
#     longest_path = 0
#
#     for s in strs:
#         update_paths = {}
#         for point, val in paths.items():
#             vec = (s.count("0"), s.count("1"))
#             vec_path = (vec[0] + point[0], vec[1] + point[1])
#
#             if (vec_path[0] > m) or (vec_path[1] > n):
#                 continue
#
#             if paths.get(vec_path, 0) < val +1:
#                 update_paths[vec_path] = val +1
#                 if val +1 > longest_path:
#                     longest_path = val+1
#
#
#         paths.update(update_paths)
#
#     return longest_path

def findMaxForm(self, strs: List[str], m: int, n: int):
    paths = {(0, 0, 0)}
    for s in strs:
        sm = s.count("0")
        sn = s.count("1")
        paths |= {(length+1, sm+em, sn+en) for i, em, en in paths if sm+em<=m and sn+en<=n}
    return max(path_length for path_length, _, _ in paths)
