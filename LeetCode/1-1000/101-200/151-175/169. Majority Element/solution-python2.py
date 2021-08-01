from typing import List
from collections import deque


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # Let's try to do this in a more sensible way...

        # if there are only 1 or 2 elements in the list
        # the first item is necessarily the majority
        if len(nums) < 3:
            return nums[0]
        deq = deque(nums)
        temp = []
        current_val = deq.popleft()
        while deq:
            if current_val != deq[0]:
                deq.popleft()
                current_val = temp.pop() if temp else deq.popleft()
            else:
                temp.append(current_val)
                current_val = deq.popleft()
        return current_val
