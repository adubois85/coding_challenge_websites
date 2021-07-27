from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # it feels like cheating using Python built-in stuff, but...
        # if not nums2 or n == 0:
        #     nums1 = nums1[0:m]
        # elif not m == 0:
        #     nums1 = nums2[0:n]
        # else:
        #     temp = nums1[0:m] + nums2[0:n]
        #     temp.sort()
        #     nums1 = [v for v in temp]

        # stupid Python copying of variables instead of altering things
        # in place as one would expect
        for i in range(len(nums1) - m):
            nums1.pop()
        for i in nums2[0:n]:
            nums1.append(i)
        nums1.sort()
