class Solution:
    def countSpecialIntegers(self, nums: list[int]) -> int:
        temp=set()
        n=len(nums)
        d={}
        ans=0
        for i in nums:
            d[i]=d.get(i,0)+1

        i=0
        while i<n:
            j=i
            while j<n and nums[i]==nums[j]:
                j+=1
            if d[nums[i]]==j-i:
                ans+=1
            i=j
        return ans
            