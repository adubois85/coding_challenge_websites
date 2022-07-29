class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # copy/paste from the fastest solution on LeetCode.
        # It is faster than what I did, probably because it isn't constantly 
        # slicing lists, but it's about 2x slower than what it was listed at in
        # the after-problem chart (64ms vs 31ms).
        start = 0
        res = 0
        dic = {}
        for i, c in enumerate(s):
            if c in dic and start <= dic[c]:
                start = dic[c]+1
            else:
                res = max(res, i-start+1)
            dic[c] = i
        return res

