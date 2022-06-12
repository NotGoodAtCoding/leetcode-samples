def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
    ans = []

    def dfs(root, height):
        if not root:
            return

        nonlocal ans
        if height >= len(ans):
            ans.append([])
        ans[height].append(root.val)

        dfs(root.left, height+1)
        dfs(root.right, height+1)

    dfs(root, 0)
    return ans
