class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        ans=[]
        m=len(mat)
        n=len(mat[0])
        row=col=0
        flag=0
        for i in range(m*n):
            ans.append(mat[row][col])
            if flag==0:
                if col==n-1:
                    row+=1
                    flag=1
                elif row==0:
                    col+=1
                    flag=1
                else:
                    row-=1
                    col+=1
            else:
                if row==m-1:
                    col+=1
                    flag=0
                elif col==0:
                    row+=1
                    flag=0
                else:
                    row+=1
                    col-=1
        return ans