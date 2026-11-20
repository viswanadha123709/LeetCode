class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x=0
        y=0
        p='north'
        for i in instructions:
            if i=='G':
                if p=='north':
                    y+=1
                elif p=='south':
                    y-=1
                elif p=='east':
                    x+=1
                else:
                    x-=1
            elif i=='L':
                if p=='north':
                    p='west'
                elif p=='south':
                    p='east'
                elif p=='east':
                    p='north'
                else:
                    p='south'
            else:
                if p=='north':
                    p="east"
                elif p=='south':
                    p='west'
                elif p=='east':
                    p='south'
                else:
                    p='north'

        if x==y==0 or p!='north':
            return True
        return False


            