class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        m=len(matrix)
        n=len(matrix[0])
        ans=0
        dp=[[0]*n for i in range(m)]

        def dfs(row,col):
            if dp[row][col]!=0:
                return dp[row][col]
            c1=c2=c3=c4=1
            if row<m-1 and matrix[row+1][col]>matrix[row][col]:
                if dp[row+1][col]!=0:
                    c1+=dp[row+1][col]
                else:
                    c1+=dfs(row+1,col)
            if row>0 and matrix[row-1][col]>matrix[row][col]:
                if dp[row-1][col]!=0:
                    c2+=dp[row-1][col]
                else:
                    c2+=dfs(row-1,col)
            if col<n-1 and matrix[row][col+1]>matrix[row][col]:
                if dp[row][col+1]!=0:
                    c3+=dp[row][col+1]
                else:
                    c3+=dfs(row,col+1)
            if col>0 and matrix[row][col-1]>matrix[row][col]:
                if dp[row][col-1]!=0:
                    c4+=dp[row][col-1]
                else:
                    c4+=dfs(row,col-1)
            dp[row][col]=max(c1,c2,c3,c4)
            return dp[row][col]

        for i in range(m):
            for j in range(n):
                ans=max(ans,dfs(i,j))

        return ans