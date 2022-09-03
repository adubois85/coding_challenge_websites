class Solution:
    def intToRoman(self, num: int) -> str:
        numerals = [(1000, 'M'),
                    (900, 'CM'),
                    (500, 'D'),
                    (400, 'CD'),
                    (100, 'C'),
                    (90, 'XC'),
                    (50, 'L'),
                    (40, 'XL'),
                    (10, 'X'),
                    (9, 'IX'),
                    (5, 'V'),
                    (4, 'IV'),
                    (1, 'I')]
        pos = 0
        roman = ''
        while num > 0:
            while num >= numerals[pos][0]:
                num -= numerals[pos][0]
                roman += numerals[pos][1]
            pos += 1
        return roman
