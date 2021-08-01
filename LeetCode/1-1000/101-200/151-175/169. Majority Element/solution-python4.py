from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # a more proper implementation of the
        # Boyer-Moore majority voting algorithm
        counter = 0
        majority = None
        for i in range(len(nums)):
            if counter == 0:
                majority = nums[i]
                counter = 1
            elif majority == nums[i]:
                counter += 1
            else:
                counter -= 1
        return majority
