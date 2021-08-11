from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # I'm pretty sure this is how LeetCode actually wants you to solve
        # this.  Reverse the entire list, then reverse the first k elements,
        # and finally reverse the elements from k to the end.
        # You can't just use the reversed built-in because Python does that
        # goofy thing again where it creates a copy of the list being passed
        # instead of working on it in-place as you would expect.  Python at
        # least makes swapping variables pretty easy.
        end = len(nums)
        if k >= end:
            k = k % end
        if k == 0:
            return
        l, r = 0, end - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        l, r = 0, k - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
        l, r = k, end - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l, r = l + 1, r - 1
