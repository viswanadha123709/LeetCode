class Solution:
    def countRotations(self, s: str, k: int) -> int:
        n=len(s)
        s+=s[:n-1]
        ans=0
        
        for i in range(n):
            score=0
            for j in range(i,i+n-1):
                if s[j]==s[j+1]:
                    score+=1
            if score==k:
                ans+=1
        return ans
    