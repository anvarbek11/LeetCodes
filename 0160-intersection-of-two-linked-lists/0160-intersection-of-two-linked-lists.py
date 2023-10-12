# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        b1,b2 = headA, headB
        while b1 != b2:
            b1=b1.next if b1 else headB
            b2=b2.next if b2 else headA
        return b1    