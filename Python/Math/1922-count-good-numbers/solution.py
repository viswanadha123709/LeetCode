mod=(10**9)+7
class Solution:
    def countGoodNumbers(self, n: int) -> int:
        odd=n//2
        even=n-odd
        return (pow(5,even,mod)*pow(4,odd,mod)%mod)
    