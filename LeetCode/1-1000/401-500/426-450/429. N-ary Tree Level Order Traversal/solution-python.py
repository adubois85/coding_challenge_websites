from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # This is a spin-off of my third solution to LeetCode #589.  Once I had
    # that one working, this was just a few minutes of tweaking to get working.
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root:
            return root
        order, level = [], []
        order.append([root.val])
        current = deque(root.children)
        children = deque()
        while current:
            temp = current.popleft()
            if temp.children:
                for child in temp.children:
                    children.append(child)
            level.append(temp.val)
            if not current:
                order.append(level)
                level = []
                current = children
                children = deque()
        return order
