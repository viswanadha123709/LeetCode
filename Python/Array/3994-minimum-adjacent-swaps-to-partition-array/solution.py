class Solution:
    def minAdjacentSwaps(self, nums: list[int], a: int, b: int) -> int:
        minis=0
        maxis=0
        ans=0
        for i in nums:
            if i<a:
                ans=(ans+minis+maxis)%(10**9+7)
            elif a<=i<=b:
                ans=(ans+maxis)%(10**9+7)
                minis+=1
            else:
                maxis+=1
        return ans
            
            
        