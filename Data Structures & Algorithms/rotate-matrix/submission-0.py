class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        row=len(matrix)
        col=len(matrix[0])
        for i in range(row):
            for j in range(i):
                matrix[i][j],matrix[j][i]=matrix[j][i],matrix[i][j]

        for i in range(row):
            for j in range(col//2):
                matrix[i][j],matrix[i][col-1-j]=matrix[i][col-1-j],matrix[i][j]


                
        