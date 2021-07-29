from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        # Without lots of temp variables
        if not nums:
            return None
        temp = TreeNode()
        # go left
        temp.left = self.sortedArrayToBST(nums[:len(nums)//2])
        # go right
        temp.right = self.sortedArrayToBST(nums[(len(nums)//2 + 1):len(nums)])
        temp.val = nums[len(nums)//2]
        return temp
