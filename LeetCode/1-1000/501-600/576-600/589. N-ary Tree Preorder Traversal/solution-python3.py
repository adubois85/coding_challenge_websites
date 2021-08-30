from typing import List
from collections import deque


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # A better solution, this one doesn't use recursion.  Instead, we're using
    # a stack of sorts.  Add a node to the ordered list, then append any of
    # that node's children to the front of the stack.  Technically, I'm using a
    # double-ended queue because a bit of testing showed it was faster than
    # using lists, regardless of whether I was adding to and removing from the
    # front or back of the stack.
    def preorder(self, root: 'Node') -> List[int]:
        if not root:
            return root
        order = [root.val]
        deq = deque(root.children)
        while deq:
            temp = deq.popleft()
            if temp.children:
                # have to use the reverse, otherwise you get the children from
                # right to left because of how they're added to the stack
                for child in reversed(temp.children):
                    deq.appendleft(child)
            order.append(temp.val)
        return order
