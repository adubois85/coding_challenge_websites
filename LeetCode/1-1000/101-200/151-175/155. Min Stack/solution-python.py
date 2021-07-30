class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        # Current top of stack
        self.top_val = None
        # Next item down the stack
        # Should end up being a tuple of tuples
        self.previous_val = None
        # Current smallest value on the stack
        self.min_val = None

    def push(self, val: int) -> None:
        self.previous_val = (self.top_val, self.min_val, self.previous_val)
        # In some cases at least, Python treats None and 0 as equivalent
        if self.min_val is None or val < self.min_val:
            self.min_val = val
        self.top_val = val

    def pop(self) -> None:
        self.top_val = self.previous_val[0]
        self.min_val = self.previous_val[1]
        self.previous_val = self.previous_val[2]

    def top(self) -> int:
        return self.top_val

    def getMin(self) -> int:
        return self.min_val


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
