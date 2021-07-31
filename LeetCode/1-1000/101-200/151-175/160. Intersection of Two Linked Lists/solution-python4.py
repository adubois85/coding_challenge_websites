# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        # Using a counting method, just to see how it compares
        count_a = 0
        count_b = 0
        pa = headA
        pb = headB
        while pa:
            count_a += 1
            pa = pa.next
        while pb:
            count_b += 1
            pb = pb.next
        pa = headA
        pb = headB
        if count_a < count_b:
            count_a = count_b - count_a
            while count_a != 0:
                count_a -= 1
                pb = pb.next
        else:
            count_b = count_a - count_b
            while count_b != 0:
                count_b -= 1
                pa = pa.next
        while pa != pb:
            print(f"pa is {pa.val} and pb is {pb.val}")
            pa = pa.next
            pb = pb.next
        return pa
