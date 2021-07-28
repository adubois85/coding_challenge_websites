from typing import List


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


# [1, 2, 3, 4, 5, 6, 7, 8, 9]
#              5
#        3           7
#     2     4     6     8
#  1                       9
# [6, 7, 8, 9]
# [7, 8, 9]
# []
class Solution:
    def sortedArrayToBST(self, nums: List[int]) -> TreeNode:
        if not nums:
            return None
        end = len(nums)
        mid = end//2
        temp = TreeNode()
        # go left
        if 0 < mid < end:
            temp.left = self.sortedArrayToBST(nums[0:mid])
        # go right
        if mid < (mid + end)//2 < end:
            temp.right = self.sortedArrayToBST(nums[(mid + 1):end])
        temp.val = nums[mid]
        return temp
