from typing import List


# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children

# Copy / paste from one of the other solutions on LeetCode
# One of the reasons I had so many problems getting this to work is because of
# how the input data was set up.  After poking around with print statements, I
# found out this is how it was actually represented on the site:
# Input = Node(1, [Node(3, [Node(5, []), Node(6, [])]), Node(2, []), Node(4, [])])
# Notably, for nodes with no children, they still have an empty list as their
# child.  Even when using an accepted answer, I couldn't get it to work in my
# test space due to "'NoneType' object is not iterable."  Frustrating that I
# spent so much time troubleshooting when it was down to weird, unexpected
# inputs.  I mean, look at the definition for the Node class--it shows that the
# default value for children should be None, not an empty list.
class Solution:
    def preorder(self, root: 'Node') -> List[int]:
        arr = []
        self.preorderRecursive(root, arr)
        return arr

    def preorderRecursive(self, root, arr):
        if(root is None):
            return
        arr.append(root.val)
        for child in root.children:
            self.preorderRecursive(child, arr)
