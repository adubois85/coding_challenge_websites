from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # Slight elaboration of my first solution.  It fixes what I mentioned
        # in the comment, duplicating work due to checking indices that have no
        # way of fulfilling the requirements, by skipping them entirely.
        i = 0
        while i < (end := len(flowerbed)):
            prev = (0 if (i - 1) < 0 else flowerbed[i - 1])
            next = (0 if (i + 1) > end - 1 else flowerbed[i + 1])
            if next == 1:
                i += 2
            elif prev + flowerbed[i] + next == 0:
                i += 1
                n -= 1
            i += 1
        if n > 0:
            return False
        return True
