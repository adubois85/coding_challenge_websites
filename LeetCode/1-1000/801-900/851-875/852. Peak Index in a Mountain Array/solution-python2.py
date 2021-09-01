from typing import List


class Solution:
    # Second verse, same as the first--but this time with a binary search.  And
    # yet somehow it's slower than the first?  Probably from all of the
    # comparisons.  Then again, I re-submitted it and now it's faster, so who
    # even knows?  In theory, at least, this is now O(log(n)) time complexity.
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        start = 0
        end = len(arr)
        while start != end:
            index = (start + end) // 2
            if arr[index - 1] < arr[index] > arr[index + 1]:
                start = end = index
            elif arr[index] > arr[index + 1]:
                end = (start + end) // 2
            else:
                start = ((start + end) // 2) + 1
        return index
