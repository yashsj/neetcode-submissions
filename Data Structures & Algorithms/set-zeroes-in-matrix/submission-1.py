class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        setrow=False
        row=len(matrix)
        column=len(matrix[0])
        for i in range(row):
            for j in range(column):
                if matrix[i][j]==0:
                    matrix[0][j]=0
                    if i!=0:
                        matrix[i][0]=0
                    else:
                        setrow=True
        
        for j in range(1,column):
            if matrix[0][j]==0:
                for i in range(row):
                    matrix[i][j]=0
        
        for i in range(1,row):
            if matrix[i][0]==0:
                for j in range(column):
                    matrix[i][j]=0

        if matrix[0][0]==0:
            for i in range(row):
                matrix[i][0]=0
        if setrow:
            for j in range(column):
                matrix[0][j]=0

        
        