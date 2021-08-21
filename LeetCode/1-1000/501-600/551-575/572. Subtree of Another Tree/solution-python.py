from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # With a heavy assist from this video:
    # https://www.youtube.com/watch?v=HdMs2Fl_I-Q
    # Still feels like there should be a way to do this without a helper function
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if not root:
            return False
        if self.is_same(root, subRoot):
            return True
        return self.isSubtree(root.left, subRoot) or self.isSubtree(root.right, subRoot)

    def is_same(self, tree, subTree):
        if not tree or not subTree:
            return tree is None and subTree is None
        if tree.val == subTree.val:
            return self.is_same(tree.left, subTree.left) and self.is_same(tree.right, subTree.right)
        return False
