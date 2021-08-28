class Solution:
    # Did this one because it only took me a few minutes to throw together
    # after seeing it in the list of problems.  A bit esoteric, using Python's
    # slice notation to get everything in the string before and after any
    # letters that need to be lowercased, and chr(), ord(), and some math to
    # change an uppercase ASCII character into its lowercase equivalent.  Also,
    # f-strings.
    def toLowerCase(self, s: str) -> str:
        for i in range(len(s)):
            if 64 < (ord(s[i])) < 91:
                s = f"{s[:i]}{chr(ord(s[i]) + 32)}{s[i + 1:]}"
        return s
