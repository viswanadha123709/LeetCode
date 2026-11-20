class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        mini,maxi=min(nums),max(nums)
        temp=set(nums)
        ans=[]
        for i in range(mini+1,maxi):
            if i not in temp:
                ans.append(i)
        return ans
        