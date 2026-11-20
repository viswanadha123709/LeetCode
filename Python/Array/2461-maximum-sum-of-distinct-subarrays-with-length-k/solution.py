class Solution:
    def maximumSubarraySum(self, arr: List[int], k: int) -> int:
        ans=0
        d={}
        curr=0
        for i in range(k):
            d[arr[i]]=d.get(arr[i],0)+1
            curr+=arr[i]
        if len(d)==k:
            ans=max(ans,curr)
        
        for i in range(k,len(arr)):
            d[arr[i]]=d.get(arr[i],0)+1
            d[arr[i-k]]-=1
            curr+=arr[i]
            curr-=arr[i-k]
            if d[arr[i-k]]==0:
                d.pop(arr[i-k])
            if len(d)==k:
                ans=max(ans,curr)

        return ans
            



            