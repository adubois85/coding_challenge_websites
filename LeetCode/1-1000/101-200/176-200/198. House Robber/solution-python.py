from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # This is another dynamic programming problem.  This is very similar to
        # LeetCode problem #53, Maximum Subarray.  There, you were basically
        # asking what was the largest sum possible for the subarray ending on
        # that index of the main array.  Here, you are asking more or less the
        # same thing, with the caveat that you have to skip the adjacent index.
        if len(nums) == 1:
            return nums[0]
        one_back = nums[0]
        two_back = current = 0
        for i in range(1, len(nums)):
            current = max(nums[i] + two_back, one_back)
            two_back = one_back
            one_back = current
        return current
