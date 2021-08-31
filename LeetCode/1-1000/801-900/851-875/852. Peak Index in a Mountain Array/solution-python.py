from typing import List


class Solution:
    # Braindead simple solution, but slow-ish.  O(n) time complexity.
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        index = 1
        while arr[index] < arr[index + 1]:
            index += 1
        return index
