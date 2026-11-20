class Solution(object):
    def minEatingSpeed(self, piles, h):
        """
        :type piles: List[int]
        :type h: int
        :rtype: int
        """
        def valid(mid):
            hours=0
            for i in piles:
                hours+=(i+mid-1)//mid
            return hours<=h
            
        low=1
        high=sum(piles)
        while(low<=high):
            mid=(low+high)>>1
            if valid(mid):
                high=mid-1
                ans=mid
            else:
                low=mid+1
        return ans
        
                
            
                