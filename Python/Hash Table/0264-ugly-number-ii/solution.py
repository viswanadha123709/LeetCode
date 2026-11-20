class Solution:
    def nthUglyNumber(self, n: int) -> int:
        dp=[1]
        i2=i3=i5=0
        while len(dp)<n:
            two=2*dp[i2]
            three=3*dp[i3]
            five=5*dp[i5]
            dp.append(min(two,three,five))
            if dp[-1]==two:
                i2+=1
            if dp[-1]==three:
                i3+=1
            if dp[-1]==five:
                i5+=1
        return dp[-1]

