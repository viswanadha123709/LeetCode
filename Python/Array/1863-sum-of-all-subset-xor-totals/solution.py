class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        ans=0
        n=len(nums)
        for i in range(2**n):
            temp=0
            for j in range(31):
                if (i>>j)&1==1:
                    temp^=nums[j]
            ans+=temp
            
        return ans
                
