from typing import List
from math import gcd


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # An array juggling algorithm
        # I never want to see another array in my life
        # I also attached the notebook I was using to test things
        # over the past few days for a slight glimpse into the maddness
        end = len(nums)
        if k >= end:
            k = k % end
        if k == 0:
            return
        for i in range(gcd(end, k)):
            temp = nums[i]
            j = i
            offset = (j - k) % end
            while i != offset:
                nums[j] = nums[offset]
                j = offset
                offset = (offset - k) % end
            nums[j] = temp
