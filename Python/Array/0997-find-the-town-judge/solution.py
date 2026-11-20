class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        maxi=0
        ele=0
        d={}
        if n==1 and not trust:
            return 1
        temp=set()
        for i in trust:
            u,v=i[0],i[1]
            temp.add(u)
            if v in d:
                d[v].append(u)
            else:
                d[v]=[u]
        for i in d:
            if len(d[i])>maxi:
                maxi=len(d[i])
                ele=i
        if maxi==n-1 and ele not in temp:
            return ele
        else:
            return -1
        