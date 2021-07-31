# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None


class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
        if not headA or not headB:
            return None
        # How do you get 2 linked lists of different lengths to line up
        # since you can't just use len/count/etc.?
        # You can move through each to the end, keeping count of the number of 
        # elements along the way and taking the difference of those as the offset.
        # Or, you can go through each separately; then upon reaching the 
        # end, start at the beginning of the other list.  Each pointer will
        # move through len(a) + len(b) and will naturally line up with the 
        # offset of their lengths after each reaches the end of their first
        # list.
        point_a = headA
        point_b = headB
        # this is super hacky, but it works
        # probably a better way to do it
        loop_a = True
        loop_b = True
        while point_a != point_b:
            point_a = point_a.next
            point_b = point_b.next
            if not point_a and loop_a:
                point_a = headB
                loop_a = False
            if not point_b and loop_b:
                point_b = headA
                loop_b = False
        return point_a
