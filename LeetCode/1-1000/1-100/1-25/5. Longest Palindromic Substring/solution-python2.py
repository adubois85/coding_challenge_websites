class Solution:
    # With an assist from the NeetCode youtube channel.
    # https://www.youtube.com/watch?v=XYQecbcd6_c
    # I had thought of this, but dismissed it as dealing with the edge cases
    # seemed inelegant; that I'd have to simply repeat the code for even and
    # odd length palindromes, which, yeah, but it's still faster.
    def longestPalindrome(self, s: str) -> str:
        longest_l, longest_r = 0, 1
        for i in range(len(s)):
            # for odd-length palindromes
            l, r = i - 1, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(s[longest_l:longest_r]):
                    longest_l, longest_r = l, r + 1
                l -= 1
                r += 1
            # for even-length palindromes
            l, r = i, i + 1
            while l > -1 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > len(s[longest_l:longest_r]):
                    longest_l, longest_r = l, r + 1
                l -= 1
                r += 1
        return s[longest_l:longest_r]
