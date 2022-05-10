def removeDuplicates(self, s: str, k: int) -> str:
    stack = []  # List[str, int] of (char, count)

    for c in s:
        if stack and c == stack[-1][0]:
            stack[-1][1] += 1
        else:
            stack.append([c, 1])
        if stack[-1][1] == k:
            stack.pop()

    out = ""
    for c, count in stack:
        out += (c * count)

    return out
