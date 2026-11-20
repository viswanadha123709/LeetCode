# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countDominantNodes(self, root: TreeNode | None) -> int:
        cnt=[0]
        def dfs(source):
            if source is None:
                return 0
            l=dfs(source.left)
            r=dfs(source.right)
            ans=max(l,r,source.val)
            if source.val==ans:
                cnt[0]+=1
            return ans
        dfs(root)
        return cnt[0]
                
            
            
                
            