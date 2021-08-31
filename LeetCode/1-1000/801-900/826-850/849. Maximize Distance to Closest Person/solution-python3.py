import itertools
from typing import List


class Solution:
    # copy / paste from one of the "fastest" solutions on LeetCode
    def maxDistToClosest(self, seats: List[int]) -> int:
        # This is basically doing the same thing I did, but in a more concise
        # way.  Firstly, find the first index of 1 from both the start and end
        # of the input array.  Then, using the itertools groupby method, gather
        # all of the runs of 1's and 0's together.  Finally, do the same math
        # to find the halfway point of each and return the largest run.
        ans = seats.index(1)
        seats.reverse()
        ans = max(ans, seats.index(1))
        for seat, group in itertools.groupby(seats):
            if not seat:
                K = len(list(group))
                ans = max(ans, (K + 1) / 2)
        return int(ans)
