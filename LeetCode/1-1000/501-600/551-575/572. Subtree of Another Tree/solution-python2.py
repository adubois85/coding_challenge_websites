from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    # Copy / paste (and cleaned up a lot) from one of the "fastest" solutions
    # This is esoteric to the max but immensely fascinating.
    # Basically, create a string representation of each tree then check if the
    # subRoot's string is contained in the root's string.
    # It seems to avoid the problem of a partial match (as in the second
    # example) both by having each leaf start with "A" and by fully filling out
    # the tree with "Z" for any empty children.
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def stringify(node):
            return f"A{node.val}{stringify(node.left)}{stringify(node.right)}" if node else "Z"
        return stringify(subRoot) in stringify(root)
