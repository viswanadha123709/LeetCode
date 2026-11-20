class Solution:
    def createGrid(self, m: int, n: int, k: int) -> list[str]:
        def checking(arr):
            if arr[0][0] == '#' or arr[m-1][n-1] == '#':
                return 0
            dp = [[0] * n for _ in range(m)]
            dp[0][0] = 1
            for i in range(1, m):
                if arr[i][0] != '#':
                    dp[i][0] = dp[i-1][0]
            for j in range(1, n):
                if arr[0][j] != '#':
                    dp[0][j] = dp[0][j-1]
            for i in range(1, m):
                for j in range(1, n):
                    if arr[i][j] != '#':
                        dp[i][j] = dp[i-1][j] + dp[i][j-1]
            return dp[m-1][n-1]

        matrix=[['.']*n for i in range(m)]
        if checking(matrix)<k:
            return []
        if checking(matrix)==k:
            return ["".join(row) for row in matrix]

        if m == 1:
            if k == 1:
                return ["." * n]
            return []
        
        if n == 1:
            if k == 1:
                return ["."] * m
            return []

        if m == 2 and n == 2:
            if k == 2:
                return ["..",
                        ".."]
            if k == 1:
                return ["..",
                        "#."]
            return []





        if m==2 and n==3:
            if k==1:
                return["...","##."]
            if k==2:
                return["...","#.."]
            if k==3:
                return["...","..."]
            
        matrix=[['#']*n for i in range(m)]
        matrix[-1][-1]='.'
        matrix[0][0]='.'
        if m==2 and n>3:
            for i in range(n):
                matrix[0][i]='.'
            if k==1:
                return ["".join(row) for row in matrix]
                
            matrix[1][-2]='.'
            if k==2:
                return ["".join(row) for row in matrix]
            matrix[1][-3]='.'
            if k==3:
                return ["".join(row) for row in matrix]
            matrix[1][-4]='.'
            if k==4:
                return ["".join(row) for row in matrix]

        if n==2 and m==3:
            for i in range(m):
                matrix[i][-1]='.'
            if k==1:
                return ["".join(row) for row in matrix]
            matrix[1][0]='.'
            if k==2:
                return ["".join(row) for row in matrix]
            matrix[2][0]='.'
            if k==3:
                return ["".join(row) for row in matrix]


        if n==2 and m>3:
            for i in range(m):
                matrix[i][-1]='.'
            if k==1:
                return ["".join(row) for row in matrix]
            matrix[1][0]='.'
            if k==2:
                return ["".join(row) for row in matrix]
            matrix[2][0]='.'
            if k==3:
                return ["".join(row) for row in matrix]
            matrix[3][0]='.'
            if k==4:
                return ["".join(row) for row in matrix]
                
            
            
                
            
            
                
            
            
            
            

            




        matrix=[['#']*n for i in range(m)]
        for i in range(n):
            matrix[0][i]='.'
        for i in range(m):
            matrix[i][-1]='.'
        if k==1:
            return ["".join(row) for row in matrix]
        matrix[1][-2]='.'
        if k==2:
            return ["".join(row) for row in matrix]
        matrix[1][-3]='.'
        if k==3:
            return ["".join(row) for row in matrix]
        matrix[0][-1]='#'
        matrix[2][-2]='.'
        return ["".join(row) for row in matrix]
        
        
        
        
        
        
            

        
            
                
                
            
            
                
            









            
        