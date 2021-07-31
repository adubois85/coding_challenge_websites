# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        hash_table = []
        while headA:
            if headA in hash_table:
                return headA
            hash_table.append(headA)
            headA = headA.next
            if headB:
                if headB in hash_table:
                    return headB
                hash_table.append(headB)
                headB = headB.next
        while headB:
            if headB in hash_table:
                return headB
            # Don't need to keep adding headB into the hash table as there are
            # no more entries in headA to check them against
            headB = headB.next
        return None
