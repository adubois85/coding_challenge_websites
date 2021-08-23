from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # Copy / paste from one of the faster solutions on LeetCode
        # This is basically what I was trying to do, but much more elegant.
        # The thing I missed that this cleverly does is if either root is None,
        # it returns the other root.  This means you don't have to iterate over
        # each node if one subtree is significantly smaller than the other, it
        # just appends the larger subtree and stops checking that branch.  And
        # if both are None, it still just returns None.
        if root1 is None or root2 is None:
            return root1 or root2
        return TreeNode(root1.val + root2.val,
                        self.mergeTrees(root1.left, root2.left),
                        self.mergeTrees(root1.right, root2.right))
