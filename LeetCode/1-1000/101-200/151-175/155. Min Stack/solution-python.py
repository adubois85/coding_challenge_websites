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
        # Need to consider the number of times an item has been added to the stack
        self.val_counts = {}

    def push(self, val: int) -> None:
        self.val_counts.setdefault(val, 0)
        self.val_counts[val] += 1
        if val < self.min_val:
            self.min_val = val
        self.top_val = val
        self.previous_val = (self.top_val, self.previous_val)

    def pop(self) -> None:
        pass

    def top(self) -> int:
        pass

    def getMin(self) -> int:
        pass


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
