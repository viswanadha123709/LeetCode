from sortedcontainers import SortedList
import heapq as hq
class Solution:
    def busiestServers(self, k: int, arrival: List[int], load: List[int]) -> List[int]:
        s=SortedList(range(k))
        heap=[]
        count=[0]*k
        for i in range(len(arrival)):
            preffered=i%k

            while heap and heap[0][0]<=arrival[i]:
                lasttime,index=hq.heappop(heap)     
                s.add(index)
            temp=s.bisect_left(preffered)
            if not s:
                continue
            if temp==len(s):
                temp=0
            index=s[temp]
            s.remove(index)
            count[index]+=1
            hq.heappush(heap,[arrival[i]+load[i],index])
        ans=[]
        maxi=max(count)
        for i in range(len(count)):
            if count[i]==maxi:
                ans.append(i)
        return ans
            