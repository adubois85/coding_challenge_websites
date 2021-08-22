from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children


class Solution:
    # Not quite functional yet, returns list of lists of lists with no simple
    # way to flatten them that's obvious to me.  Putting this on the shelf for
    # bit to work on the next problem
    def preorder(self, root: 'Node') -> List[int]:
        order = [root.val]
        if root.children:
            for i, leaf in enumerate(root.children):
                # print(i, leaf)
                order.append(self.preorder(leaf))
        return order
