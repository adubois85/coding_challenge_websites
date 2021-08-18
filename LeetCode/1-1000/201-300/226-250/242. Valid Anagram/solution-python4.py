class Solution:
    # copy / paste from the supposed 'fastest' solution
    # I somehow doubt it
    # it also breaks for anything that isn't a lowercase Latin character
    def isAnagram(self, s: str, t: str) -> bool:
        # the Unicode code points for 'a' to 'z'
        for n in range(97, 123):
            if s.count(chr(n)) != t.count(chr(n)):
                return False
        return True
