class Solution:
    # A method of splitting an integer into its contituent digits and returns
    # them as a list.  From some testing, it seems to be slower than the string
    # conversion method below.  On the other hand, this is probably more
    # portable as not every language lets you swap between strings and ints
    # so easily
    def int_split(self, num: int) -> list:
        units = []
        digit = 10
        while num != 0:
            temp = num % digit
            num -= temp
            temp = temp / (digit / 10)
            units.append(int(temp))
            digit *= 10
        return units

    def split_sum(self, num: int) -> int:
        temp = list(str(num))
        for i in range(len(temp)):
            x = int(temp[i])
            temp[i] = x * x
        return sum(temp)

    def isHappy(self, n: int) -> bool:
        values = []
        while n not in values:
            values.append(n)
            n = self.split_sum(n)
        if n == 1:
            return True
        return False
