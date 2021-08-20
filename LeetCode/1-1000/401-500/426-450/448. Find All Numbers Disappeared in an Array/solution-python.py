from typing import List
from collections import Counter


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        x = Counter(nums)
        temp = []
        for i in range(1, len(nums) + 1):
            if i not in x:
                temp.append(i)
        return temp
