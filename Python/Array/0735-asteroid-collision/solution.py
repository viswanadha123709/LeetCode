class Solution:
    def asteroidCollision(self,arr:List[int])->List[int]:
        stack=[]
        for i in arr:
            while stack and stack[-1]>0 and i<0:
                if stack[-1]<-i:
                    stack.pop()
                    continue
                elif stack[-1]==-i:
                    stack.pop()
                break
            else:
                stack.append(i)
        return stack