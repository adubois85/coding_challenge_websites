class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # Ah, dynamic programming, we meet again.  I flubbed it initially because
        # I reset the substring when it encountered a duplicate instead of
        # starting the new substring from the index after the duplicate.
        if len(s) == 0:
            return 0
        ans = 0
        substr = []
        for i in s:
            if i in substr:
                ans = max(ans, len(substr))
                substr = substr[(substr.index(i) + 1):]
            substr.append(i)
        return max(ans, len(substr))
