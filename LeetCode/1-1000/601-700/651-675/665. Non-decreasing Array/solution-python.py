from typing import List


class Solution:
    # This is so ugly and inelegant, just lots of if/else blocks checking a
    # number and its neighbors and to figure out what number to change.
    # On the other hand, if it's stupid but it works, is it really that
    # stupid?  Yeah, it still kind of is I think.
    # It's still in the 90th percentile for speed by LeetCode's metrics, so I
    # guess everyone else somehow did it even worse than this.
    def checkPossibility(self, nums: List[int]) -> bool:
        if len(nums) < 3:
            return True
        increasing = 1
        for i in range(1, len(nums) - 1):
            if nums[i - 1] > nums[i]:
                if nums[i] > nums[i + 1]:
                    return False
                elif increasing == 1:
                    increasing = 0
                else:
                    return False
            elif nums[i] > nums[i + 1]:
                if increasing == 0:
                    return False
                if nums[i - 1] > nums[i + 1]:
                    nums[i + 1] = nums[i]
                else:
                    nums[i] = nums[i + 1]
                increasing = 0
        return True
