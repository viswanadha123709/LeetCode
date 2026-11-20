class Solution:
    def maximumLength(self, nums: List[int]) -> int:
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        ans=1
        for i in d:
            if i!=1:
                temp=i
                curr=0
                while(True):
                    if temp not in d:
                        break
                    if d[temp]==1:
                        curr+=1
                        break
                    else:
                        curr+=2
                    if temp>10**9:
                        break
                    temp*=temp
                if curr%2==0:
                    curr-=1
                ans=max(ans,curr)
            else:
                curr=d[1]
                if curr%2==0:
                    curr-=1
                ans=max(ans,curr)
        return ans



