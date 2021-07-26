from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # naive
        # if len(nums) == 1:
        #     return nums[0]
        # sum = 0
        # for i, j in zip(nums, nums[1:]):
        #     if i + j > -1:
        #         sum += j
        # return sum
        # super naive
        sum = nums[0]
        if len(nums) = 1:
            return sum
        for i in range(len(nums)):
            temp = 0
            for j in range(i, len(nums)):
                temp += nums[j]
                if temp > sum:
                    sum = temp
        return sum
