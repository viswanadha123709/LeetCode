class Solution(object):
    def minimizedMaximum(self, n, quantities):
        """
        :type n: int
        :type quantities: List[int]
        :rtype: int
        """
        
        def valid(mid):
            total=0
            for i in quantities:
                total+=(i+mid-1)//mid
            return total<=n

        low=1
        high=max(quantities)
        ans=0
        while(low<=high):
            mid=(low+high)>>1
            if valid(mid):
                high=mid-1
                ans=mid
            else:
                
                low=mid+1
        return ans

                