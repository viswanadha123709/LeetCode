class Solution:
    def minOperations(self, s: str) -> int:
        n=len(s)
        permi=[]
        ans=n*26
        for i in range(n):
            temp=s[i:]+s[:i]
            permi.append(temp)
        for i in range(n):
            temp=permi[i]
            low=0
            high=n-1
            curr=i
            while low<high:
                a=ord(temp[low])
                b=ord(temp[high])
                mini=min(a,b)-ord("a")
                maxi=max(a,b)-ord("a")
                first=maxi-mini
                second=26-maxi+mini
                curr+=min(first,second)
                low+=1
                high-=1
            ans=min(ans,curr)
        return ans
                