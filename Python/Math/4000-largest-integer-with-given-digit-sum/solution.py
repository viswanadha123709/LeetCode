class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        req=s
        curr=0
        for i in range(n):
            if req<9:
                curr*=10
                curr+=req
                req=0
            else:
                curr*=10
                curr+=9
                req-=9
        
        if req==0:
            return curr
        else:
            return -1
            
            
            