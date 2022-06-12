def isBalanced(self, root: Optional[TreeNode]) -> bool:
    bal = True
    def dfs(root):
        # if not bal, return 
        if not root:
            return 0
        lheight = dfs(root.left)
        rheight = dfs(root.right)

        nonlocal bal
        if abs(lheight - rheight) > 1:
            bal = False

        return 1 + max(lheight, rheight)

    dfs(root)
    return bal
