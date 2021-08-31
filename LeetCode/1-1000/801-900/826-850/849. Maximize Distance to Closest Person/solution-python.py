from typing import List


class Solution:
    # I very quickly realized that I didn't need to do any complicated checking
    # of how far a 1 is from each side of a 0 or anything.  When you break down
    # the problem, what you're looking for are runs of 0's and then finding the
    # longest run with a few caveats.  For runs on either edge, you can just
    # add the number as-is since Alex would sit at the edge and have all the
    # seats between him and the next person, but for runs in the middle, Alex
    # would sit in the middle of the longest run.  Due to how the question is
    # phrased, this means we need to take the ceiling of the half for runs that
    # are odd-lengthed, and just the half for even-lengthed runs.
    def maxDistToClosest(self, seats: List[int]) -> int:
        counts = []
        counter = 0
        first = 0 if seats[0] == 0 else 1
        for i in range(len(seats)):
            if seats[i] == 0:
                counter += 1
            else:
                if first == 1:
                    if counter % 2 == 0:
                        # floor division so we get an int; otherwise you'd get
                        # a float and would need to call int() on the return
                        counter = counter // 2
                    else:
                        # janky ceiling division; do floor division on the
                        # inverse, then invert it back to a positive number
                        counter = -(-counter // 2)
                counts.append(counter)
                first = 1
                counter = 0
        # if the seats array ends with a 0, it will never hit the logic to add
        # that last run to the count list, so we do it here
        if counter != 0:
            counts.append(counter)
        return max(counts)
