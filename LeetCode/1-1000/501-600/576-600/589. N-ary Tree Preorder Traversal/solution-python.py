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
    # def preorder(self, root: 'Node') -> List[int]:
    #     order = [root.val]
    #     if root.children:
    #         for i, leaf in enumerate(root.children):
    #             # print(i, leaf)
    #             order.append(self.preorder(leaf))
    #     return order

    # This works but is ugly and slow as hell.  Pylama also complains that it's
    # too complex (too much branching logic)
    def preorder(self, root: 'Node') -> List[int]:
        try:
            if root.children is None:
                return root.val
        except AttributeError:
            return root
        order = [root.val]
        temp = []
        if root.children:
            try:
                for leaf in root.children:
                    temp.append(self.preorder(leaf))
                    # print(temp)
            except TypeError:
                temp.append(self.preorder(root.children))
            for num in temp:
                if type(num) is list:
                    for j in range(len(num)):
                        order.append(num[j])
                else:
                    order.append(num)
                # temp = self.preorder(leaf.children)
        return order
