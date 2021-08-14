# This is way more clever than anything I could devise, but it makes sense.
# Copied straight from one of the top answers and formatted slightly
class Solution:
    def countPrimes(self, n: int) -> int:
        # create a list of True values, except for the first 2 to account for
        # n of 0 or 1.
        # n - 2 because:
        #   1 less due to indexing starting at 0
        #   1 less because it's a non-inclusive range, e.g. if n = 31, we don't
        #       want to include 31 in the count of primes because 31 is not
        #       itself less than 31.
        prime = [False] * 2 + [True] * (n - 2)
        # This is a slightly more elegant way of doing a square root without
        # having to import the math library.  One more than that to assure that
        # we're above the square root of n.  We only have to eliminate numbers
        # starting from the square of a prime, and thus can also stop when the
        # square of a prime > n (i.e. if a prime is greater than the square
        # root of n), because all composite numbers between a prime and its
        # square will have already been eliminated by a smaller prime.  This is
        # easier to see with a visualization.
        for i in range(2, int(n ** 0.5) + 1):
            if prime[i]:
                # slice notation with a step parameter
                prime[i*i:n:i] = [False] * ((n - 1 - i * i) // i + 1)
                # As noted above, from a prime's square to the end of the array
                # with the prime number as the step.  The math for how many
                # False values to create is confusing to look at but makes more
                # sense when you remember order of operations.  But basically,
                # n - 1 because of the zero-indexing again, minus square of the
                # prime, our starting value, floor division of that by our
                # prime to get the number of whole factors, then add one I
                # think because this range does need to be inclusive of our
                # start and end numbers
        # I didn't realize that Python's sum function works on truthy values
        return sum(prime)
