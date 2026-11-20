# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        
        temp=ListNode(None)
        head=temp
        while(True):
            mini=float('inf')
            idx=-1
            for i in range(len(lists)):
                if lists[i] and lists[i].val<mini:
                    mini=lists[i].val
                    idx=i
            if idx==-1:
                break
            temp.next=lists[idx]
            temp=temp.next
            lists[idx]=lists[idx].next
            
        return head.next
            
