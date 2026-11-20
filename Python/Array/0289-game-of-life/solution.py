class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m=len(board)
        n=len(board[0])
        def checking(row,column):
            count=0
            if row<m-1 and board[row+1][column] in [1,2]:
                count+=1
            if row>0 and board[row-1][column] in [1,2]:
                count+=1
            if column<n-1 and board[row][column+1] in [1,2]:
                count+=1
            if column>0 and board[row][column-1] in [1,2]:
                count+=1
            if row>0 and column>0 and board[row-1][column-1] in [1,2]:
                count+=1
            if row<m-1 and column<n-1 and board[row+1][column+1] in [1,2]:
                count+=1
            if row>0 and column<n-1 and board[row-1][column+1] in [1,2]:
                count+=1
            if row<m-1 and column>0 and board[row+1][column-1] in [1,2]:
                count+=1
            return count
        
        for i in range(m):
            for j in range(n):
                if checking(i,j)<2:
                    if board[i][j]==1:
                        board[i][j]=2
                if checking(i,j) in [2,3]:
                    if board[i][j]==0 and checking(i,j)==3:
                        board[i][j]=-1
                if checking(i,j)>3:
                    if board[i][j]==1:
                        board[i][j]=2
        for i in range(m):
            for j in range(n):
                if board[i][j] in [1,-1]:
                    board[i][j]=1
                else:
                    board[i][j]=0


        
                
        