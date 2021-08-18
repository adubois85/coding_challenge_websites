from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # recursive solution
    # Depth-first search going right, then left
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if root is None:
            return root
        if root.right:
            self.invertTree(root.right)
        if root.left:
            self.invertTree(root.left)
        root.left, root.right = root.right, root.left
        return root
