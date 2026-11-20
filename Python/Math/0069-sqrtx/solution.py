class Solution:
    def mySqrt(self, x: int) -> int:
        
        p1=0
        p2=x
        ans=0
        while(p1<=p2):
            mid=(p1+p2)>>1
            if mid*mid<=x:
                ans=mid
                p1=mid+1
            else:
                p2=mid-1
        return ans

        