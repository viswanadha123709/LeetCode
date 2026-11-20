class Solution:
    def countTriplets(self, arr: List[int]) -> int:
        n=len(arr)
        ans=0
        for i in range(n):
            curr=0
            for j in range(i,n):
                curr^=arr[j]
                if curr==0:
                    ans+=(j-i)
        return ans