# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumEvenGrandparent(self, root: Optional[TreeNode]) -> int:
        summ=[0]
        def iterate(root):
            if root is None:
                return
            a=0
            b=0
            c=0
            d=0
            if root.val&1==0:
                if root.left:
                    if root.left.left:
                        a=root.left.left.val
                    if root.left.right:
                        b=root.left.right.val
                if root.right:
                    if root.right.left:
                        c=root.right.left.val
                    if root.right.right:
                        d=root.right.right.val

            summ[0]+=(a+b+c+d)
            iterate(root.left)
            iterate(root.right)
        iterate(root)
        return summ[0]

        