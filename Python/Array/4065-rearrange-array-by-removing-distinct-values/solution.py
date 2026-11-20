class Solution:
    def rearrangeArray(self, nums: list[int]) -> list[int]:
        ans=[]
        d={}
        for i in nums:
            d[i]=d.get(i,0)+1
        while d:
            curr=sorted(list(d.keys()))
            for i in curr:
                ans.append(i)
                d[i]-=1
                if d[i]==0:
                    d.pop(i)
                
        return ans