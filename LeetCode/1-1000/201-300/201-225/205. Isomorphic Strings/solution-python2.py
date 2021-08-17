class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # Copy / paste from the "fastest" solution.
        # It's sort of beautiful in its simplicity, if wildly esoteric.
        # Basically the same thing as the hacky failsafe in my first solution;
        # compare the number of unique characters in each string with the
        # number of unique characters in a zip of both strings.  If there's a
        # mismatch in any of them, they can't be isomorphic.
        return len(set(zip(s, t))) == len(set(s)) == len(set(t))