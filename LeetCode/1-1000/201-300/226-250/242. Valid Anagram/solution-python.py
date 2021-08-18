class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # if the strings aren't the same length, they can't be anagrams
        if len(s) != len(t):
            return False
        # creating lists from each string and sorting them should result in the
        # same list if they're anagrams; should also be robust and work for any
        # Unicode string, not just lowercase Latin characters.
        if sorted(list(s)) != sorted(list(t)):
            return False
        return True
