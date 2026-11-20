class Solution:
    def jobScheduling(self, startTime: List[int], endTime: List[int], profit: List[int]) -> int:
        import heapq as hq
        n=len(startTime)
        jobs=[[startTime[i],endTime[i],profit[i]] for i in range(n)]
        jobs.sort()
        heap=[]
        best=0
        for i in range(n):
            
            while heap and heap[0][0]<=jobs[i][0]:
                u=hq.heappop(heap)
                best=max(best,u[1])
            curr=best+jobs[i][2]
            hq.heappush(heap,[jobs[i][1],curr])
        
        while heap:
            u=hq.heappop(heap)
            best=max(best,u[1])

        return best

