class Solution:
    def checkDivisibility(self, n: int) -> bool:
        def check(n):
            summ=0
            prod=1
            while n>0:
                summ+=n%10
                prod*=n%10
                n//=10
            return summ,prod
        summ,prod=check(n)
        if n%(summ+prod)==0:
            return True
        else:
            return False