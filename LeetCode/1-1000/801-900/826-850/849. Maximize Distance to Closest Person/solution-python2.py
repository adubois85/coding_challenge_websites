from typing import List


class Solution:
    # Slightly cleaned-up version of my first solution, mainly simplifying and
    # rearranging the logic when seats[i] == 1.  Thanks to one of the other
    # solutions on LeetCode, I realized that I can just add 1 to the counter
    # and I'll get the correct number whether it's odd or even.
    def maxDistToClosest(self, seats: List[int]) -> int:
        counts = []
        counter = 0
        first = 0 if seats[0] == 0 else 1
        for i in range(len(seats)):
            if seats[i] == 0:
                counter += 1
            else:
                if first == 0:
                    first = 1
                    # Multiply by 2 since we're going to divide it by 2 next
                    counter *= 2
                counter = (counter + 1) // 2
                counts.append(counter)
                counter = 0
        if counter != 0:
            counts.append(counter)
        return max(counts)
