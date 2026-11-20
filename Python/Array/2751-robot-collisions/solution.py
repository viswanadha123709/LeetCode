class Solution:
    def survivedRobotsHealths(self, positions: List[int], healths: List[int], directions: str) -> List[int]:
        tempi=positions.copy()
        for i in range(len(positions)):
            positions[i]=[positions[i],healths[i],directions[i]]
        positions.sort(key=lambda x: x[0])
        stack=[]
        for i in range(len(positions)):
            while stack and stack[-1][2]=='R' and positions[i][2]=='L':
                if stack[-1][1]==positions[i][1]:
                    stack.pop()
                    break
                elif stack[-1][1]>positions[i][1]:
                    stack[-1][1]-=1
                    break
                else:
                    positions[i][1]-=1
                    stack.pop()
            else:
                stack.append(positions[i])

        d={}
        for robot in stack:
            d[robot[0]] = robot[1]
        ans=[]
        for i in tempi:
            if i in d:
                ans.append(d[i])
        return ans

        
    
        
