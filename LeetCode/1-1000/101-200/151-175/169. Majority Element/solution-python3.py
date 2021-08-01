from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Let's try to do this in a more sensible way...

        # if there are only 1 or 2 elements in the list
        # the first item is necessarily the majority
        if len(nums) < 3:
            return nums[0]
        temp = []
        current_val = nums.pop()
        # now with 100% less double-ended queue
        while nums:
            if current_val != nums[-1]:
                nums.pop()
                current_val = temp.pop() if temp else nums.pop()
            else:
                temp.append(current_val)
                current_val = nums.pop()
        return current_val
