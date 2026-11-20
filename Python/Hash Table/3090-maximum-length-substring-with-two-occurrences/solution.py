class Solution:
    def maximumLengthSubstring(self, s: str) -> int:
        ans=0
        left=0
        d={}
        n=len(s)
        for i in range(n):
            d[s[i]]=d.get(s[i],0)+1
            while d[s[i]]>2:
                d[s[left]]-=1
                left+=1
            ans=max(ans,i-left+1)
        return ans

        
        