from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        if len(nums) == 1:
            return TreeNode(nums[0])
        end = len(nums)
        mid = end//2
        temp = TreeNode()
        # go left
        temp.left = self.sortedArrayToBST(nums[0:mid])
        # go right
        temp.right = self.sortedArrayToBST(nums[(mid + 1):end])
        temp.val = nums[mid]
        return temp
