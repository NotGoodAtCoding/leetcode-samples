Check if a binary tree is balanced by performing a dfs to determine the relative heights of each subtree, and if the differences exceed 1, then it's unbalanced.

Since the dfs implementation is recursive, it doesn't allow for short breaking as is, but it could be added by returning from all dfs calls once it is determined that the tree is not balanced.
