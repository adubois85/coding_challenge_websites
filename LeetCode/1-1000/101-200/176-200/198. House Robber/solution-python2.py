from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        # a slightly more concise version on the first solution.
        # should also be a touch faster.
        one_back = two_back = 0
        for i in nums:
            current = max(i + two_back, one_back)
            two_back = one_back
            one_back = current
        return current
