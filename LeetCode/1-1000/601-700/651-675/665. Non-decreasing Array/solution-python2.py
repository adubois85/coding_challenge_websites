from typing import List


class Solution:
    # copy / paste with cleanup from one of the supposed "fastest" solutions
    # It's definitely more elegant, though.  It basically moves all of those
    # checks I was doing to the end instead of cluttering up the main body of
    # the function.  Submitting it, though, appeared to show that it's exactly
    # as fast as my first solution and somehow slightly worse on memory.
    def checkPossibility2(self, nums: List[int]) -> bool:
        count = 0
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                index = i
                count += 1
                if count == 2:
                    return False
        if count == 0:
            return True
        if index == 0 or index == len(nums) - 2:
            return True
        if nums[index - 1] <= nums[index + 1]:
            return True
        if nums[index] <= nums[index + 2]:
            return True
        return False
