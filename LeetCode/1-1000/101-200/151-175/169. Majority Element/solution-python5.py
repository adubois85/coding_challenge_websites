from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # because of course Python has a built-in function
        # to do this in its standard library
        c = Counter(nums)
        return c.most_common(1)[0][0]
