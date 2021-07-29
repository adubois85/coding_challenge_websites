# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def hasCycle(self, head: ListNode) -> bool:
        # There is a more mathematical way to approach it,
        # but I was going about it the wrong way, trying to
        # add values and use modulos and such.
        # This created problems with 0 values.
        # Instead, using two pointers moving at different rates,
        # they will meet at some common multiple of the cycle length,
        # if there is one.
        while head:
            try:
                slow = head.next
                fast = head.next.next
            except:
                return False
            if slow == fast:
                return True
            head = head.next
        return False
