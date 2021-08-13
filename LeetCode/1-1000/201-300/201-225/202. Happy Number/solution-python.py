class Solution:
    # A method of splitting an integer into its contituent digits and returns
    # them as a list.  From some testing, it seems to be slower than the string
    # conversion method below.  On the other hand, this is probably more
    # portable as not every language lets you swap between strings and ints
    # so easily
    def int_split(num: int) -> list:
        units = []
        digit = 10
        while num != 0:
            temp = num % digit
            num -= temp
            temp = temp / (digit / 10)
            units.append(int(temp))
            digit *= 10
        return units

    def isHappy(self, n: int) -> bool:
        temp = list(str(n))
        for i in range(len(temp)):
            x = int(temp[i])
            temp[i] = x * x
        return temp
