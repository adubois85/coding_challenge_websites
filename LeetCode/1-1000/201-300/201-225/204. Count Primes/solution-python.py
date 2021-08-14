class Solution:
    def countPrimes(self, n: int) -> int:
        # doing things the hard way
        nums = set()
        count = 0
        for i in range(2, n):
            # print(i)
            if i in nums:
                pass
            else:
                count += 1
                nums.add(i)
                j = i * i
                nums.add(j)
                while j < n:
                    j += i
                    nums.add(j)
        return count
