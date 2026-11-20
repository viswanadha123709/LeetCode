# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
        po_index=[len(inorder)-1]

        hm={}
        for i in range(len(inorder)):
            hm[inorder[i]]=i

        def tree(root,l,r):
            if l>r:
                return None
            if root is None:
                root=TreeNode(postorder[po_index[0]])
            
            pos=hm[postorder[po_index[0]]]
            po_index[0]-=1

            root.right=tree(root.right,pos+1,r)
            root.left=tree(root.left,l,pos-1)
            return root
        
        root=None
        root=tree(root,0,len(inorder)-1)
        return root