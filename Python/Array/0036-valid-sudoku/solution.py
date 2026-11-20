class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        def check(arr):
            for i in arr:
                for j in i:
                    if i.count(j)>1 and j!=".":
                        return False
            temp=set()
            for i in range(9):
                for j in range(9):
                    if arr[j][i] in temp and arr[j][i]!=".":
                        return False
                    else:
                        temp.add(arr[j][i])
                temp=set()
            
            for i in [0,3,6]:
                for j in [0,3,6]:
                    for k in range(i,i+3):
                        for l in range(j,j+3):
                            if arr[k][l] in temp and arr[k][l]!=".":
                                return False
                            else:
                                temp.add(arr[k][l])
                    temp=set()
            return True

        return check(board)

            

            