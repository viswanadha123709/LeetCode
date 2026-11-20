class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        ans=0
        while start or goal:
            a=start&1
            b=goal&1
            if a!=b:
                ans+=1
            start>>=1
            goal>>=1
        return ans

