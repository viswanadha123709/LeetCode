class Solution:
    def countKConstraintSubstrings(self, s: str, k: int) -> int:
        n=len(s)
        ans=0
        left=one=zero=0
        for i in range(n):
            if s[i]=='1':
                one+=1
            else:
                zero+=1
            while one>k and zero>k:
                if s[left]=='0':
                    zero-=1
                else:
                    one-=1
                left+=1
            ans+=i-left+1
        return ans