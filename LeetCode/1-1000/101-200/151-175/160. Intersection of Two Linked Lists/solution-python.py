# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        # Super slow and naive double-nested loop
        # But there is definitely a better way to go about this
        temp = headB
        while headA:
            while headB:
                if headA == headB:
                    return headA
                headB = headB.next
            headA = headA.next
            headB = temp
        return None