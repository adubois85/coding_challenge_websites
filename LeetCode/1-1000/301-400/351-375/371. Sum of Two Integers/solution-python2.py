class Solution:
    # The supposed 'fastest' solution from LeetCode
    # I imagine this is how they wanted you to solve this problem, using
    # bitwise operators to manipulate the binary bits directly.
    # Still, I'm surpised by how close my lumbering behemoth,
    # "enterprise edition," of a solution is speed and memory usage
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xffffffff
        # works both as while loop and single value check
        while (b & mask) > 0:
            carry = (a & b) << 1
            a = (a ^ b)
            b = carry
        # handles overflow
        return (a & mask) if b > 0 else a
