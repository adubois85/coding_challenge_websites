from typing import Optional


# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    # Perhaps not the most elegant, but it gets the job done.  It's easier to go through each
    # linked list in turn, extract the values, then pad the resulting lists to be equal rather
    # than trying to move through each at the same time and handling non-existant next nodes.
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1, list2 = [], []
        while l1:
            list1.append(l1.val)
            l1 = l1.next
        while l2:
            list2.append(l2.val)
            l2 = l2.next
        diff = len(list1) - len(list2)
        if diff > 0:
            list2 = list2 + [0] * diff
        else:
            list1 = list1 + [0] * abs(diff)
        head = next = ListNode((list1[0] + list2[0]) % 10)
        carry = (list1[0] + list2[0]) // 10
        for i in range(1, len(list1)):
            next.next = ListNode((list1[i] + list2[i] + carry) % 10)
            carry = (list1[i] + list2[i] + carry) // 10
            next = next.next
        if carry != 0:
            next.next = ListNode(1)
        return head

