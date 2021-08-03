class Solution:
    def trailingZeroes(self, n: int) -> int:
        # I guess the important thing to note is that the number of trailing
        # zeroes should only ever increase.  Also, the only numbers that
        # should increase the number of zeroes are mulitples of 5.
        # Where it gets interesting is that certain multiples of 5 will
        # increase the number of trailing zeroes by more than 1, e.g. 25
        # will add 2 more zeroes.
        
        # Ultimately what it comes down to is factors of 2 and 5, because
        # 2 x 5 = 10.  Since every even number can be factored down to 2,
        # the 5's are the limiting factor.  The tricky thing I noted above
        # is because some numbers have multiple factors of 5, e.g.
        # 25 = 5 x 5.  So we need to find all the factors of 5, and then
        # find how many of those also have factors of 5 (5^2, 5^3, etc.), and
        # so on down the line
        total = 0
        while n > 4:
            # floor division because we don't care about the remainders
            n = n // 5
            total += n
        return total
