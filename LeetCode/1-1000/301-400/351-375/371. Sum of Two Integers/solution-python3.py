from math import log, exp


class Solution:
    # another copy/paste from one of the apparently 'fastest' solutions
    # I like this one because it's clever, arguably too clever as it's not
    # immediately obvious what's going on.  It takes advantage of the fact that
    # multiplying two numbers of the same base is equal to that base to the sum
    # of their exponents, e.g. a^2 x a^3 = a^(2+3)
    # This takes e to the power of each number and multiplies them, then
    # reverses that by taking the natural log of their product.  Finally, you
    # use the int function to convert the float back to an integer.
    def getSum(self, a: int, b: int) -> int:
        return int(log(exp(a)*exp(b)))