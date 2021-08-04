from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # A better way is to copy just the value at the point where
        # the rotation will start to a temp variable, overwrite it
        # with the rotated value, then write that temp variable to
        # the place of the original rotation value, and repeat.
        # storing this as a variable isn't necessary, but it's easier to read
        ln = len(nums)
        if k >= ln:
            k = k % ln
        temp = None
        ln = ln - k
        for i in range(k):
            temp = nums[i]
            nums[i] = nums[ln + i]
            nums[ln + i] = temp

# [6, 7, 8, 9, 1, 2, 3, 4, 5]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [6, 2, 3, 4, 5, 1, 7, 8, 9]
# [6, 7, 3, 4, 5, 1, 2, 8, 9]
# [6, 7, 8, 4, 5, 1, 2, 3, 9]
# [6, 7, 8, 9, 5, 1, 2, 3, 4]

# [7, 8, 9, 1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [7, 2, 3, 4, 5, 6, 1, 8, 9]
# [7, 8, 3, 4, 5, 6, 1, 2, 9]
# [7, 8, 9, 4, 5, 6, 1, 2, 3]

# [7, 8, 9, 1, 5, 6, 4, 2, 3]
# [7, 8, 9, 1, 2, 6, 4, 5, 3]
# [7, 8, 9, 1, 2, 3, 4, 5, 6]


# [8, 9, 1, 2, 3, 4, 5, 6, 7]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [8, 2, 3, 4, 5, 6, 7, 1, 9]
# [8, 9, 3, 4, 5, 6, 7, 1, 2]

# [8, 9, 1, 4, 5, 6, 7, 3, 2]
# [8, 9, 1, 2, 5, 6, 7, 3, 4]

# [8, 9, 1, 2, 3, 6, 7, 5, 4]
# [8, 9, 1, 2, 3, 4, 7, 5, 6]

# [8, 9, 1, 2, 3, 4, 5, 7, 6]
# [8, 9, 1, 2, 3, 4, 5, 6, 7]


# [7, 8, 9, 1, 2, 3, 4, 5, 6]
# [1, 2, 3, 4, 5, 6, 7, 8, 9]

# [7, 2, 3, 4, 5, 6, 1, 8, 9]
# [7, 8, 3, 4, 5, 6, 1, 2, 9]
# [7, 8, 9, 4, 5, 6, 1, 2, 3]

# [7, 8, 9, 1, 5, 6, 4, 2, 3]
# [7, 8, 9, 1, 2, 6, 4, 5, 3]
# [7, 8, 9, 1, 2, 3, 4, 5, 6]
