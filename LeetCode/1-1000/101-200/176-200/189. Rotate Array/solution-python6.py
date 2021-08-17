from typing import List


# A more concise version of the first solution I made
# It's apprently also faster than any other solution I created
# This problem is so, so bad and is best forgotten
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if k >= (end := len(nums)):
            k = k % end
        if k == 0:
            return
        k = end - k
        temp = nums[k:] + nums[:k]
        for i in range(end):
            nums[i] = temp[i]

