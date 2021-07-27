from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # it feels like cheating using Python built-in stuff, but...
        if not nums2 or n == 0:
            nums1 = nums1[0:m]
        elif not m == 0:
            nums1 = nums2[0:n]
        else:
            nums1 = nums1[0:m] + nums2[0:n]
            nums1.sort()