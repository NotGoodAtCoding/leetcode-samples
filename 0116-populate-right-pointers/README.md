This is a BFS implementation.

We go level by level by continually selecting the leftmost node as "cur" and use "nxt" to store the next level node. At the root, this is just the root node and it's left child. Then, using the parent node to store references, we set the parent's left child "next" to the right child. If there is a "next" on the current node (which will be set when the parent is processed) then the right child's "next" of the parent node will be the parent node's next's left child. Then, we attempt to move on to the next node. If there is no next node, we are at the end of the level and should therefore drop a level by setting the cur node to its left child.

```
def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    # init cur to root node, next level to the left child
    cur, nxt = root, root.left if root else None

    # as long as there is a next level to traverse
    while nxt:
        # left child next set to right child
        cur.left.next = cur.right

        # the right child is set to the cur's sibling's left child
        if cur.next:
            cur.right.next = cur.next.left

        # continue the BFS by setting the next level
        cur = cur.next
        if not cur:
            cur = nxt
            nxt = cur.left

    return root

```

The BFS is made easier by populating the next pointer on the level below in order to use that information while traversing. 
