class Solution:
    def reverseWords(self, s: str) -> str:
        # Using Python's built-in string manipulation methods
        # Split the string into words at the spaces, reverse and join the
        # individual words, then rejoin the words with a space
        s = s.split(' ')
        for i, word in enumerate(s):
            s[i] = ''.join(list(reversed(word)))
        return ' '.join(s)
