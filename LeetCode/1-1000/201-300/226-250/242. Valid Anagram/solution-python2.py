class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        temp = list(s)
        # I though my first solution was janky, but using try/except blocks?
        # It also seems to be significantly slower, though a bit better on
        # the memory as I don't have to create a list for each string.
        for char in t:
            try:
                temp.remove(char)
            except ValueError:
                return False
        return True
