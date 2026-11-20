class Solution:
    def findBall(self, grid: List[List[int]]) -> List[int]:
        ans=[]
        n=len(grid[0])
        m=len(grid)
        for ball in range(n):
            i=ball
            level=0
            if (i==0 and grid[level][i]==-1) or (i==n-1 and grid[level][i]==1):
                ans.append(-1)
                continue
            while level<m and 0<=i<n:
                if (i==0 and grid[level][i]==-1) or (i==n-1 and grid[level][i]==1):
                    break
                elif grid[level][i]==1 and grid[level][i+1]==1:
                    level+=1
                    i+=1
                elif grid[level][i]==-1 and grid[level][i-1]==-1:
                    level+=1
                    i-=1
                else:
                    break

            if level==len(grid):
                ans.append(i)
            else:
                ans.append(-1)
        return ans
            


            
            