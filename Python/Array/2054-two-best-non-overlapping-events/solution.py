class Solution:
    def maxTwoEvents(self, events: List[List[int]]) -> int:
        events.sort()
        dp=[[None]*3 for i in range(len(events))]

        def path(index,remaining):
            if remaining==0 or index==len(events):
                return 0

            if dp[index][remaining] is not None:
                return dp[index][remaining]

            skip=path(index+1,remaining)

            low=index+1
            high=len(events)-1

            while(low<=high):
                mid=(low+high)>>1
                if events[mid][0]>events[index][1]:
                    high=mid-1
                else:
                    low=mid+1

            keep=path(low,remaining-1)

            ans=max(skip,keep+events[index][2])
            dp[index][remaining]=ans
            return ans

        return path(0,2)