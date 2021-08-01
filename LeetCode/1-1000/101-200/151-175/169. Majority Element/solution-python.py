from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        # naive to the extreme
        num_set = {}
        for i in nums:
            num_set.setdefault(i, 0)
            num_set[i] += 1
        return list(num_set.keys())[list(num_set.values()).index(max(num_set.values()))]
