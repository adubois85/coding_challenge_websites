# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # # Super naive approach
        if not l1:
            return l2
        if not l2:
            return l1
        lsorted = temp = ListNode()
        while l1 and l2:
            if l1.val < l2.val:
                temp.next = ListNode(l1.val)
                l1 = l1.next
            else:
                temp = ListNode(l2.val)
                l2 = l2.next
            temp = temp.next
        if l1:
            temp.next = l1
        while l2:
            temp.next = l2
        return temp.next
