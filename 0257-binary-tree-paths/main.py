def binaryTreePaths(root: Optional[TreeNode]) -> List[str]:
    paths = []
    if not root:
        return paths
    if (not root.right) and (not root.left):
        # This is a leaf
        paths.append(str(root.val))
    if root.right:
        # append result of subtree on right
        paths.extend([f"{root.val}->{subpath}" for subpath in self.binaryTreePaths(root.right)])
    if root.left:
        # append result of subtree on left
        paths.extend([f"{root.val}->{subpath}" for subpath in self.binaryTreePaths(root.left)])
    return paths
