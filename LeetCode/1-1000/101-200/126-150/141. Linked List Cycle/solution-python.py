# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # naive, but I'm sure there's a more mathematical way to approach it
        table = []
        while head:
            if head in table:
                return True
            else:
                table.append(head)
                head = head.next
        return False
