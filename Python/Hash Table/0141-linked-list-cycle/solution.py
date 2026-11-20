# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        temp=head
        for i in range(10**4+1):
            if temp and temp.next:
                temp=temp.next
            else:
                return False
        return True
        