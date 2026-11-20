class Solution:
    def maxValue(self, events: List[List[int]], k: int) -> int:
        events.sort()
        val=[[None]*len(events) for i in range(k+1)]
        def path(index,remaining):
            if remaining==0 or index==len(events):
                return 0
            if val[remaining][index] is not None:
                return val[remaining][index]
            skip=path(index+1,remaining)
            curr=events[index][2]
            p1=index+1
            p2=len(events)-1
            while(p1<=p2):
                mid=(p1+p2)>>1
                if events[mid][0]>events[index][1]:
                    p2=mid-1
                else:
                    p1=mid+1
            take=path(p1,remaining-1)+curr
            ans=max(take,skip)
            val[remaining][index]=ans
            return ans
        return path(0,k)
        
            




        