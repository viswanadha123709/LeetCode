class Solution:
    def validPath(self, n: int, edges: List[List[int]], source: int, destination: int) -> bool:
        d={}
        for i in range(n):
            d[i]=[]
        for i in edges:
            u,v=i[0],i[1]
            d[u].append(v)
            d[v].append(u)
        visited=set()
        found=[False]
        def dfs(source,destination):
            visited.add(source)
            if source==destination:
                found[0]=True
            for i in d[source]:
                if i not in visited:
                    dfs(i,destination)
        dfs(source,destination)
        return True if found[0] else False