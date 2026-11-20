class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n=len(arr)
        if n<3:
            return 0
        ans=0
        temp=1
        while temp<n:
            up=0
            down=0
            while temp<n and arr[temp]>arr[temp-1]:
                up+=1
                temp+=1
            while temp<n and arr[temp]<arr[temp-1]:
                down+=1
                temp+=1

            if up>0 and down>0:
                ans = max(ans,up+down+1)
            if up==0 and down==0:
                temp+=1

        return ans