from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def mergeTrees(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> Optional[TreeNode]:
        # This feels so clunky, but it's the only surefire way I can think of
        # right now to ensure I'm not trying to get the attribute of a Nonetype
        # object and erroring out.  Well, execpt for a big stack of try/except
        # blocks, which I did try while I was messing about...
        if root1 is None and root2 is None:
            return None
        r1_val = 0 if root1 is None else root1.val
        r2_val = 0 if root2 is None else root2.val
        merged = TreeNode(r1_val + r2_val)
        r1_left = None if not root1 else root1.left
        r2_left = None if not root2 else root2.left
        merged.left = self.merge(r1_left, r2_left)
        r1_right = None if not root1 else root1.right
        r2_right = None if not root2 else root2.right
        merged.right = self.merge(r1_right, r2_right)
        return merged
