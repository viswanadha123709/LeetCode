class Solution(object):
    def repairCars(self, ranks, cars):
        """
        :type ranks: List[int]
        :type cars: int
        :rtype: int
        """
        low=1
        high=min(ranks)*(cars**2)
        ans=high
        def valid(time):
            total = 0

            for r in ranks:
                total += int((time //r) ** 0.5)

            return total >= cars
        while(low<=high):
            mid=(low+high)>>1
            if valid(mid):
                ans=mid
                high=mid-1
            else:
                low=mid+1
        return ans