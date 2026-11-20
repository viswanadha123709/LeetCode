class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        d={}
        ans=[]
        def dfs(visited,source,destination):
            visited.add(source)
            if source==destination:
                return True
            for i in d[source]:
                if i not in visited:
                    if dfs(visited,i,destination):
                        return True
            return False



        for i in edges:
            u,v=i[0],i[1]
            if u in d and v in d and dfs(set(),u,v):
                ans=[u,v]
            else:
                if u in d:
                    d[u].append(v)
                else:
                    d[u]=[v]
                if v in d:
                    d[v].append(u)
                else:
                    d[v]=[u]
        return ans
