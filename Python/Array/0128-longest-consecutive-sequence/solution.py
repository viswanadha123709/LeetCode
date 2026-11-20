class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hs=set(nums)
        ans=0
        for i in hs:
            if i-1 not in hs:
                curr=0
                j=i
                while(j in hs):
                    j+=1
                    curr+=1
                ans=max(ans,curr)
        return ans

