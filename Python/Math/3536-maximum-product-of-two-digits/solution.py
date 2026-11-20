class Solution:
    def maxProduct(self, n: int) -> int:
        first=second=float('-inf')
        temp=n
        while temp>0:
            i=temp%10
            if i>=first:
                second=first
                first=i
            elif first>i>second:
                second=i
            temp//=10

        return first*second
