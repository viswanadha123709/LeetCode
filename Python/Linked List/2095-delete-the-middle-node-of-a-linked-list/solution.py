# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head or not head.next:
            return None
        turtle=rabbit=head
        prev=ListNode(None)
        while(rabbit and rabbit.next):
            prev=turtle
            turtle=turtle.next
            rabbit=rabbit.next.next
        prev.next=turtle.next
        return head
