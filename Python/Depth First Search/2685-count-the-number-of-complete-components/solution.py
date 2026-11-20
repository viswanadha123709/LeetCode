class Solution:
    def countCompleteComponents(self, n: int, edges: List[List[int]]) -> int:
        d={}
        for i in range(n):
            d[i]=[]
        for i in edges:
            u,v=i
            d[u].append(v)
            d[v].append(u)
        visited=set()
        components=[0]
        degree=[0]
        def dfs(source):
            visited.add(source)
            components[0]+=1
            degree[0]+=len(d[source])
            for i in d[source]:
                if i not in visited:
                    dfs(i)

        count=0
        for i in range(n):
            components=[0]
            degree=[0]
            if i not in visited:
                dfs(i)
                c=components[0]
                deg=degree[0]
                if deg==c*(c-1):
                    count+=1
                
        return count
            