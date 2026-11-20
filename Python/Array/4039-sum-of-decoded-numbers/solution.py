import math
class Solution:
    def sumDecoded(self, nums: list[int]) -> int:
        mod=(10**9+7)
        ans=0
        for i in nums:
            width=i%10
            d=str(i//10)
            x=int(d[:width])
            y=int(d[width:])
            temp=pow(x,y,mod)
            ans=(ans+temp)%mod

        return ans
            
                