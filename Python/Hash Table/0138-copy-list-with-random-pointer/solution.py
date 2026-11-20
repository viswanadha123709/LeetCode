"""
# Definition for a Node.
class Node:
    def __init__(self, x, next=None, random=None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None

        mp = {}

        curr = head
        while curr:
            copy = Node(curr.val)
            mp[curr] = copy
            curr = curr.next

        curr = head
        while curr:
            copy = mp[curr]
            copy.next = mp.get(curr.next)
            copy.random = mp.get(curr.random)
            curr = curr.next

        return mp[head]
        