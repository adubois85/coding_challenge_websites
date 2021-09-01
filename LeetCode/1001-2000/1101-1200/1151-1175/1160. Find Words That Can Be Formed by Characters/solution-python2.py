from typing import List


class Solution:
    # Copy / paste from one of the faster solutions on LeetCode.  Instead of
    # using counters, it just uses the fact that Python is good at manipulating
    # strings with its various built-in methods.
    def countCharacters(self, words: List[str], chars: str) -> int:
        ans = 0
        for word in words:
            for ch in word:
                if word.count(ch) > chars.count(ch):
                    break
            # I never realized you could put if / else blocks on different
            # levels--and that it would actually work
            else:
                ans += len(word)
        return ans
