class Solution:
    def minimumPushes(self, word: str) -> int:
        n=len(word)
        if n<=8:
            return n
        ans=0
        curr=1
        while(n>0):
            if n<8:
                ans+=(curr*n)
                n=0
            else:
                ans+=(curr*8)
                curr+=1
                n-=8
        return ans