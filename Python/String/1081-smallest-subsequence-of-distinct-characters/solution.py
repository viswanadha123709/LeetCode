class Solution:
    def smallestSubsequence(self, s: str) -> str:
        d={}
        for i in range(len(s)):
            d[s[i]]=i
        stack=[]
        temp=set()
        for i in range(len(s)):
            if s[i] in temp:
                continue

            while stack and ord(stack[-1])>ord(s[i]) and d[stack[-1]]>i:
                temp.remove(stack.pop())  
            stack.append(s[i])
            temp.add(s[i])
        return "".join(stack)

            