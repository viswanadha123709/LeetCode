class Solution:
    def minimumCost(self, nums: list[int], k: int) -> int:
        cost=0
        carry=k
        req=0
        for i in nums:
            if carry>=i:
                carry-=i
            else:
                temp=(i-carry+k-1)//k
                req+=temp
                carry+=(k*temp)
                carry-=i
        return (req*(req+1)//2)%(10**9+7)
            
                
        
            
            
                
            