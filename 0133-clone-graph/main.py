def cloneGraph(self, node: 'Node') -> 'Node':
    # for each node
    # set node to seen in hashmap
    # copy node and neighbors
    # for each neighbor, perform the same operation unless it is already processed

    if not node:
        return None

    processed = {}

    def dfs(node):
        if node in processed:
            return processed[node]  # node already seen, return the COPY created

        copy = Node(node.val)  # create new node
        processed[node] = copy  # add copy to the map

        for n in node.neighbors:
            copy.neighbors.append(dfs(n))  # copy the neighbors
        return copy

    return dfs(node)
