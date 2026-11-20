class Solution:
    def isHappy(self, n: int) -> bool:
        temp=n

        for i in range(10**4):
            summ=0
            while(temp>0):
                summ+=(temp%10)**2
                temp//=10
            if summ==1:
                return True
            temp=summ
        return False

        

