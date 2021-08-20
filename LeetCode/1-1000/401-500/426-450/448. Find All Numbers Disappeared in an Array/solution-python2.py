from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Create a set of the numbers in the inclusive range(1, n), then do a
        # set difference (aka relative complement) of that set and the input
        # list.  That is, all the elements that are in x but not nums.  This
        # returns a set (which LeetCode accepted), but if you absolutely needed
        # a list returned, you can call list() on the return value.
        x = set(range(1, len(nums) + 1))
        return x.difference(nums)
