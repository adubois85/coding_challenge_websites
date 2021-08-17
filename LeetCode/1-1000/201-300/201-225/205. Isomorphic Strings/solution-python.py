class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        # hacky failsafe -- if the number of unique characters in each string
        # is not the same, then there's no way to transform one into the other
        # without breaking the rule of no two characters mapping to the same character
        if len(set(s)) != len(set(t)):
            return False
        # create a dictionary that maps a the first occurance of a letter in
        # the first string with its transformation in the second string.  If
        # subsequent occurances of that char don't match, we know the strings
        # aren't isomorphic
        mappings = {}
        for i in range(len(s)):
            if s[i] not in mappings:
                mappings[s[i]] = t[i]
            elif t[i] != mappings[s[i]]:
                return False
        return True
