# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # # Super naive approach
        lsorted = ListNode(0)
        while l1 is not None and l2 is not None:
            if l1.val < l2.val:
                lsorted.next = l1.val
                l1 = l1.next
            else:
                lsorted.next = l2.val
                l2 = l2.next
        while l1 is not None:
            lsorted.next = l1.val
            l1 = l1.next
        while l2 is not None:
            lsorted.next = l2.val
            l2 = l2.next
        return lsorted
