class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack=[]
        maxi=[]
        for i in operations:
            if i not in ['C','D','+']:
                stack.append(int(i))
                
            if i=='C':
                if stack:
                    stack.pop()
            if i=='D':
                stack.append(stack[-1]*2)
            if i=='+':
                stack.append(stack[-1]+stack[-2])
        return sum(stack)
                