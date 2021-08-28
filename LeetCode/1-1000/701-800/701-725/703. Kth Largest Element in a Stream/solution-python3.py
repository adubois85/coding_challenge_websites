from typing import List
import heapq


# Today on "Of Course Python Has Something Built Into the Standard Library for
# That," we have the heapq library, which implements the general heap queue
# algorithm and heaps, aka priority queues.  More or less the same thing as my
# first solution where I used a binary search to insert a value into the sorted
# list except heaps aren't as strict about order; they only require that
# heap[k] <= heap[2k + 1]
# e.g. [0, 1, 3, 4, 5, 6, 9, 8] is a valid heap because heap[3] == 4,
# which is less than heap[(2 * 3) + 1] == 8
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.k = k
        # silly mistake; this doesn't work because as mentioned above, values
        # after the first aren't guaranteed to be in strict order, just
        # generally greater than those before
        # heapq.heapify(nums)
        nums.sort()
        self.k_elements = nums[-k:]

    def add(self, val: int) -> int:
        # as before, if we don't yet have k elements, we just push the val onto
        # the heap
        if len(self.k_elements) < self.k:
            heapq.heappush(self.k_elements, val)
        else:
            # per the documentation, this is more efficient than separate heap
            # push and pop operations
            heapq.heappushpop(self.k_elements, val)
        return self.k_elements[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)
