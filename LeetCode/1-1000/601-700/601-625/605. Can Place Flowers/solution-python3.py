from typing import List


class Solution:
    # copy / paste from the supposed "fastest" solution on LeetCode
    # Sometimes the fastest isn't the best, though, as I find this significantly
    # more difficult to parse what's going on than either of my solutions
    # Also, submitting to LeetCode showed it wasn't actually faster than mine
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        index = 0
        count = 0
        while index < (end := len(flowerbed)):
            if flowerbed[index] == 1:
                index += 2
            else:
                canPut = False
                if index - 1 >= 0 and flowerbed[index - 1] == 0 \
                        and index + 1 < end and flowerbed[index + 1] == 0:
                    count += 1
                    canPut = True
                elif index == 0 and (index + 1 >= end or flowerbed[index + 1] == 0):
                    count += 1
                    canPut = True
                elif index == end - 1 and flowerbed[index - 1] == 0:
                    count += 1
                    canPut = True
                if canPut:
                    index += 2
                else:
                    index += 1
        return count >= n
