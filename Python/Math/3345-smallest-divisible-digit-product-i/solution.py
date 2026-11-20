class Solution:
    def smallestNumber(self, n: int, t: int) -> int:
        def product(n):
            if n<10:
                return n
            prod=1
            while n>0:
                prod*=(n%10)
                n//=10
            return prod
        
        for i in range(n,n+11):
            if product(i)%t==0:
                return i

