from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # the most obvious, but not best, way is to create a
        # second list startting from the rotated value,
        # then copy that back onto the original list
        temp = []
        # Rotating the list by the number of items in it is the
        # same as doing nothing.  Rotating by more that that is
        # then the same as rotating it by the modulus of those
        if k >= len(nums):
            k = k % len(nums)
        rot_end = len(nums) - k
        while k > 0:
            temp.append(nums[-k])
            k -= 1
        for i in range(rot_end):
            temp.append(nums[i])
        for i in range(len(nums)):
            nums[i] = temp[i]
