from typing import List
from collections import Counter


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        # Should be pretty self evident: create a counter for all the items,
        # then check if every number in the inclusive range(1, n) has a key in
        # the counter.  Probably because of how the keys are hashed, trying to
        # do this on the input list (e.g. if i not in nums) is significantly
        # slower than using the counter, even accounting for the time it takes
        # to build said counter.
        x = Counter(nums)
        temp = []
        for i in range(1, len(nums) + 1):
            if i not in x:
                temp.append(i)
        return temp
