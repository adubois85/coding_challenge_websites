from typing import List


class KthLargest:
    # To initialize the problem, sort the input array, then save the last k
    # elements of that list
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        # Had to modify the way I select the last k elements; if the initial
        # input list is shorter than k, it would wrap around and cause issues.
        # E.g. if the input were [1, -5] and k = 3, it k_elements would only be
        # [1] as 2 - 3 = -1, so nums[-1:] would only give the last element.
        # Realized after doing this that I can simplify it further
        # end = (len(nums) - k if len(nums) - k > 0 else 0)
        self.k_elements = nums[-k:]

    def add(self, val: int) -> int:
        # If the input list were empty, you'll get out of bounds errors as you
        # try to compare val with non-existant indices
        if not self.k_elements:
            self.k_elements.append(val)
        # If the value we're trying to add is as large or larger than the last
        # value in the sorted array, we can simply add it to the end and remove
        # the first element since val is necessarily bigger than everything
        # else in the list.
        elif val >= self.k_elements[-1]:
            self.k_elements.append(val)
        # If that isn't true, we can use a binary search to determine where to
        # put the value in our list.  If the value we're trying to add is
        # less than the smallest number in our list, we don't even have to do
        # that and can simply return whatever is already the smallest value.
        # Slight addendum, if we don't yet have k items in our list, we still
        # need to add the value regardless.
        elif val > self.k_elements[0] or len(self.k_elements) < self.k:
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
        # only need to remove things if we have more than k elements
        if len(self.k_elements) > self.k:
            self.k_elements.pop(0)
        return self.k_elements[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
