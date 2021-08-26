from typing import List


class KthLargest:
    # To initialize the problem, sort the input array, then save the last k
    # elements of that list
    def __init__(self, k: int, nums: List[int]):
        # self.k = k
        nums = sorted(nums)
        self.k_elements = nums[len(nums) - k:]

    def add(self, val: int) -> int:
        # If the value we're trying to add is as large or larger than the last
        # value in the sorted array, we can simply add it to the end and remove
        # the first element since val is necessarily bigger than everything
        # else in the list.
        if val >= self.k_elements[-1]:
            self.k_elements.pop(0)
            self.k_elements.append(val)
        # If that isn't true, we can use a binary search to determine where to
        # put the value in our list.  If the value we're trying to add is
        # less than the smallest number in our list, we don't even have to do
        # that and can simply return whatever is already the smallest value.
        elif val > self.k_elements[0]:
            start = 0
            end = len(self.k_elements)
            while start != end:
                mid = (start + end) // 2
                if val == self.k_elements[mid]:
                    start = end = mid
                elif val < self.k_elements[mid]:
                    end = mid
                else:
                    start = mid + 1
            self.k_elements.insert(end, val)
            self.k_elements.pop(0)
        return self.k_elements[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
