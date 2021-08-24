from typing import List


class Solution:
    # Not much to say about this, it's pretty straight-forward and obvious
    # what's going on.  As long as nums[i] is less than nums[i + 1], increment
    # the current counter by 1.  As soon as it's not, check if it's bigger than
    # whatever the current best is and set best to that if it is.  Also have to
    # check which is bigger at the end in case the longest subarray runs to the
    # last index because it won't hit the part that sets best in that case.
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return 1
        best = current = 1
        for i in range(len(nums) - 1):
            if nums[i] >= nums[i + 1]:
                best = max(current, best)
                current = 1
            else:
                current += 1
        return max(current, best)
