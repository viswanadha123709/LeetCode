class Solution:
    def totalNumbers(self, digits: List[int]) -> int:
        n=len(digits)
        temp=set()
        visited=[False]*(n+1)
        def fun(curr,idx,visited):
            if len(curr)==3:
                if curr[0]!=0 and curr[2] % 2 == 0:
                    temp.add(tuple(curr))
                return
            for i in range(n):
                if not visited[i]:
                    visited[i]=True
                    curr.append(digits[i])
                    fun(curr,i,visited)
                    curr.pop()
                    visited[i]=False

        fun([],0,visited)
        return len(temp)