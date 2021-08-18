from collections import Counter


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # probably the most concise you could make this, effectively one line
        return Counter(s) == Counter(t)
