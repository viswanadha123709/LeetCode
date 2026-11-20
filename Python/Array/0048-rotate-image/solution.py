class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n=len(matrix)
        for layer in range(n//2):
            for i in range(layer,n-1-layer):
                temp=matrix[layer][i]
                matrix[i][n-1-layer],temp=temp,matrix[i][n-1-layer]#b
                matrix[n-1-layer][n-1-i],temp=temp,matrix[n-1-layer][n-1-i]#c
                matrix[n-1-i][layer],temp=temp,matrix[n-1-i][layer]#d
                matrix[layer][i],temp=temp,matrix[layer][i]


        