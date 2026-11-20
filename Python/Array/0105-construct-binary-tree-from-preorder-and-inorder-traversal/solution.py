# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> Optional[TreeNode]:
        po_index=[0]
        def tree(root,l,r):
            
            if l>r:
                return None

            root=TreeNode(preorder[po_index[0]])
            pos=inorder.index(root.val)
            po_index[0]+=1
            root.left=tree(root.left,l,pos-1)
            root.right=tree(root.right,pos+1,r)
            return root
        root=None
        return tree(root,0,len(preorder)-1)