class Solution:
    # Another copy/paste job from LeetCode.  It's listed as completing in 35ms,
    # but when submitted it actually takes 85ms.  Still, I like this for the
    # use of divmod, which I'd never seen before.  Basically, give it 2
    # numbers, a and b, and return 2 other numbers:
    # a // b
    # a % b
    # In other words, how many whole multiples of b there are in a, and any
    # remainder for any partial amount.
    ROMAN = [
        (1000, "M"),
        ( 900, "CM"),
        ( 500, "D"),
        ( 400, "CD"),
        ( 100, "C"),
        (  90, "XC"),
        (  50, "L"),
        (  40, "XL"),
        (  10, "X"),
        (   9, "IX"),
        (   5, "V"),
        (   4, "IV"),
        (   1, "I"),]
    def intToRoman(self, num: int) -> str:
        result = ""
        for (arabic, roman) in self.ROMAN:
            (factor, num) = divmod(num, arabic)
            result += roman * factor
        return result
