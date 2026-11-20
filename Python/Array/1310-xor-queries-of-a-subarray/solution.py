class Solution:
    def xorQueries(self, arr: List[int], queries: List[List[int]]) -> List[int]:
        prefix=[0]
        xor=0
        ans=[]
        for i in arr:
            xor^=i
            prefix.append(xor)
        for i in queries:
            u,v=i[0],i[1]
            ans.append(prefix[v+1]^prefix[u])
        return ans