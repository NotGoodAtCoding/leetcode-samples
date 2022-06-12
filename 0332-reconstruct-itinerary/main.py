def findItinerary(self, tickets: List[List[str]]) -> List[str]:
    targets = collections.defaultdict(list)

    for a, b in sorted(tickets, reverse=True):
        targets[a].append(b)

    route, stack = [], ['JFK']
    while stack:
        while targets[stack[-1]]:
            stack.append(targets[stack[-1]].pop())
        route.append(stack.pop())
    return route[::-1]
