from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # naive
        if len(nums) == 1:
            return nums[0]
        sum = 0
        for i, j in zip(nums, nums[1:]):
            if i + j > -1:
                sum += j
        return sum