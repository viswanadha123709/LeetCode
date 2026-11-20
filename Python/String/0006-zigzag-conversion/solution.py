class Solution:
    def convert(self, s: str, numRows: int) -> str:
        d={}
        for i in range(numRows):
            d[i]=""
        temp=0
        while(temp<len(s)):
            for i in range(numRows):
                if temp>=len(s):
                    break
                d[i]+=s[temp]
                temp+=1
            for i in range(numRows-2,0,-1):
                if temp>=len(s):
                    break
                d[i]+=s[temp]
                temp+=1
        return "".join(d[i] for i in range(numRows))