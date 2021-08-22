from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        # from limited testing, using the walrus operator to set the list's
        # length is slightly faster than calculating it again in the main loop
        for i in range((end := len(flowerbed))):
            # kludgey way of checking if indices are out of range
            # on the whole, there's a lot of repeated work here, e.g. if all 3
            # equal 1, you don't need to check the next 2 indices as there will
            # be at least one 1 in the group of three
            prev = (0 if (i - 1) < 0 else flowerbed[i - 1])
            next = (0 if (i + 1) > end - 1 else flowerbed[i + 1])
            if prev + flowerbed[i] + next == 0:
                flowerbed[i] = 1
                n -= 1
        if n > 0:
            return False
        return True
