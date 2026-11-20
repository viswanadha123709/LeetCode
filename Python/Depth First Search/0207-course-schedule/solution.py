from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        d={}
        temp=[0]*numCourses
        for i in prerequisites:
            if i[1] not in d:
                d[i[1]]=[i[0]]
            else:
                d[i[1]].append(i[0])
            temp[i[0]]+=1
        q=deque()
        visited=0
        for i in range(numCourses):
            if temp[i]==0:
                q.append(i)
                visited+=1
        while q:
            u=q.popleft()
            for i in d.get(u, []):
                temp[i]-=1
                if temp[i]==0:
                    q.append(i)
                    visited+=1
        if visited==numCourses:
            return True
        return False
        

