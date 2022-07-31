class Solution:
    # I'm pretty sure this will work, but it's slow.  It exceeded the time limit on
    # LeetCode's evaluator.  Still, this feels like a dynamic programming problem,
    # but I'm not sure how to set that up.  As it is, I'm checking the same substrings
    # muliple times over, which is wildly inefficient.
    def longestPalindrome(self, s: str) -> str:
        if s == s[::-1]:
            return s
        start = None
        longest = s[0]
        for i in range(len(s)):
            end = len(s)
            if len(s[i:end]) <= len(longest):
                break
            while len(s[i:end]) > len(longest) and s[i:end] not in s[end:start:-1]:
                end -= 1
            if s[i:end] in s[end:start:-1]:
                longest = s[i:end]
            start = 0 if start is None else i - 1
        return longest
