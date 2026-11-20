class Solution:
    def judgeCircle(self, moves: str) -> bool:
        x=0
        y=0
        for i in moves:
            if i=='U':
                x+=1
            if i=='D':
                x-=1
            if i=='R':
                y+=1
            if i=='L':
                y-=1
        if x==y==0:
            return True
        else:
            return False