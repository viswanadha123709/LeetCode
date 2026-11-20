from sortedcontainers import SortedList
import heapq as hq
class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()
        s=SortedList(range(n))
        heap=[]
        count=[0]*n
        for i in range(len(meetings)):
            while heap and heap[0][0]<=meetings[i][0]:
                u,index=hq.heappop(heap)
                s.add(index)
            if not s:
                u,prefered=hq.heappop(heap)
                duration=meetings[i][1]-meetings[i][0]
                hq.heappush(heap,[u+duration,prefered])
            else:
                prefered=s[0]
                hq.heappush(heap,[meetings[i][1],prefered])
                s.remove(prefered)
            count[prefered]+=1


        maxi=max(count)
        for i in range(len(count)):
            if count[i]==maxi:
                return i
