class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        n=len(nums)
        ans=0
        d={}
        curr=0
        for i in nums:
            curr+=i
            if curr==k:
                ans+=1
            if curr-k in d:
                ans+=d[curr-k]
            d[curr]=d.get(curr,0)+1
        return ans