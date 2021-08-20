class Solution:
    def reverseWords(self, s: str) -> str:
        # Mostly a copy / paste from one of the supposed "fastest" solutions
        # Create a list from the input string reversed, and split it at spaces.
        # Then reverse that list so the word order is the same as the original
        # string, then join it back together with spaces
        word_list = s[::-1].split()
        word_list.reverse()
        return " ".join(word_list)
