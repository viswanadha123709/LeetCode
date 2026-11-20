class Solution:
    def maximumValue(self, n: int, s: int, m: int) -> int:
        temp=n-1
        total=s+(temp*m)
        excep=temp//2
        curr=total-(excep*(m+1))
        if n==1:
            return s

        
        if temp&1==0:
            return curr+1
        else:
            return curr