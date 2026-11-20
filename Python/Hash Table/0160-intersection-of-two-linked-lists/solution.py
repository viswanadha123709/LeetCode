# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA, headB):
        n1 = 0
        n2 = 0

        temp1 = headA
        temp2 = headB

        while temp1:
            n1 += 1
            temp1 = temp1.next

        while temp2:
            n2 += 1
            temp2 = temp2.next

        temp1 = headA
        temp2 = headB

        diff = abs(n1 - n2)

        if n1 > n2:
            for _ in range(diff):
                temp1 = temp1.next
        else:
            for _ in range(diff):
                temp2 = temp2.next

        while temp1 and temp2:
            if temp1 == temp2:
                return temp1

            temp1 = temp1.next
            temp2 = temp2.next

        return None
        