class Solution:
    def rearrangeString(self, s: str, x: str, y: str) -> str:
        ans=""
        for i in s:
            if i==y:
                ans=i+ans
            else:
                ans+=i
        return ans
        