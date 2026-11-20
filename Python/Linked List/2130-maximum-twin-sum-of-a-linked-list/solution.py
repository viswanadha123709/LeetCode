# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        turtle=rabbit=head
        while(rabbit and rabbit.next):
            turtle=turtle.next
            rabbit=rabbit.next.next
        
        curr=turtle
        prev=None
        while(curr):
            after=curr.next
            curr.next=prev
            prev=curr
            curr=after
        maxi=0
        while(prev and head):
            maxi=max(maxi,prev.val+head.val)
            prev=prev.next
            head=head.next
        return maxi





        