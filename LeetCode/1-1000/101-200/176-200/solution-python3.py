class Solution:
    # This will technically work, but it's slow as all get-out.
    # Worst case would be O(n^2) as you have to traverse your
    # entire list of n numbers k times, which if k is 1 less
    # than the length of nums, is effectively n.
    def rotate(self, nums, k):
        start = end = len(nums)
        if k >= start:
            k = k % start
        if k == 0:
            return
        x = 1
        while k > 0:
            k -= 1
            for i in range(1, end):
                # print(nums)
                temp = nums[-i]
                nums[-i] = nums[(-i-1) % end]
                nums[(-i-1) % end] = temp