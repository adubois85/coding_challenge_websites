from typing import List


class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        nums.sort()
        end = (len(nums) - k if len(nums) - k > 0 else 0)
        self.k_elements = nums[end:]

    # Taking a very different tack from the first solution, just add the value
    # and constantly sort the list, removing the lowest value if there are more
    # than k elements.  This works but is very slow.  On the other hand, it
    # does seem very memory efficient (at least compared to other solutions on
    # LeetCode) probably because sorting works in place.
    def add(self, val: int) -> int:
        self.k_elements.append(val)
        self.k_elements.sort()
        if len(self.k_elements) > self.k:
            self.k_elements.pop(0)
        return self.k_elements[0]


# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
