def connect(root: 'Optional[Node]') -> 'Optional[Node]':
    # traverse using BFS
    # connect children of current level via:
    # left -> right
    # once level has no left, stop traversing

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
