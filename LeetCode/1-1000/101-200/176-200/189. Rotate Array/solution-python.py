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
        start = end = len(nums)
        if k >= start:
            k = k % start
        if k == 0:
            return
        start -= k
        for i in range(end):
            temp = nums[i]
            nums[i] = nums[start]
            nums[start] = temp
            start += 1
            if start == end:
                if i + k > end:
                    start = end - 1
                else:
                    start = end - k