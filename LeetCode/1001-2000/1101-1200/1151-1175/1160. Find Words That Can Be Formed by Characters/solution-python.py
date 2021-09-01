from collections import Counter
from typing import List


class Solution:
    # Huh, it works...
    # Still, not the most efficient method, that's for certain.
    def countCharacters(self, words: List[str], chars: str) -> int:
        count = [Counter(word) for word in words]
        chars = Counter(chars)
        total = 0
        for word in count:
            temp = 0
            for k, v in word.items():
                if v > chars[k]:
                    temp -= 10000
                    break
                else:
                    temp += v
            if temp < 0:
                temp = 0
            total += temp
        return total
