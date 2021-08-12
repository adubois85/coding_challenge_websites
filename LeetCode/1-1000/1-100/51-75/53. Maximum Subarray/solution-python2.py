from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # This is a dynamic programming problem.  The tricky part, as with all
        # dynamic programming problems, is how to setup your subproblems such
        # that you don't create cyclic dependencies or exponential time growth
        # where you only need linear time.
        # About the most concise I can make this, using Python's version of
        # the ternary operator, aka conditional expressions
        current_sum = max_sum = nums[0]
        for i in range(1, len(nums)):
            current_sum = max(current_sum + nums[i], nums[i])
            max_sum = current_sum if current_sum > max_sum else max_sum
        return max_sum
