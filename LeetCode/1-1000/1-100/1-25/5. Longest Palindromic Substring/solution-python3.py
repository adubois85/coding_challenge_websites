class Solution:
    # Copy/paste from one of the fastest solution on LeetCode.  From what I can
    # tell, this is basically the same thing I'm doing, but with fewer checks.
    # Specifically, it sets the even and odd-length indices, but only checks
    # even ones if the odd one centered at that index fails, probably because
    # the odd-lengthed one will always be longer at the same center point.
    # This is seems to be a sort of implementation of Manachar's algorithm, 
    # since the size variable increasing will skip some center points, but it's
    # not a "pure" implementation of it as I've seen described online.
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        start, size = 0, 1
        for i in range(1, len(s)):
            l, r = i - size, i + 1
            s1, s2 = s[l-1:r], s[l:r] 
            if l - 1 >= 0 and s1 == s1[::-1]:
                start, size = l - 1, size + 2
            elif s2 == s2[::-1]:
                start, size = l, size + 1
                
        return s[start:start+size]