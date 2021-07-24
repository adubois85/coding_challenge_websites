# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        # Super naive approach
        self.lsorted = ListNode()
        while l1.next != None and l2.next != None:
            if l1.val < l2.val:
                self.lsorted = ListNode(l1.val)
                l1.next
            else:
                self.lsorted = ListNode(l2.val)
                l2.next
        while l1.next != None:
            self.lsorted = ListNode(l1.val)
            l1.next
        while l2.next != None:
            self.lsorted = ListNode(l2.val)
            l2.next
        return self.lsorted
