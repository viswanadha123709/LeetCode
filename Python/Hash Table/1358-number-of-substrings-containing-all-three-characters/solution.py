class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n=len(s)
        count=0
        d={'a':-1,'b':-1,'c':-1}
        if n<3:
            return 0

        for i in range(n):
            d[s[i]]=i
            count+=min(d.values())+1
        return count
