class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows=len(matrix)
        cols=len(matrix[0])
        l,r=0,rows*cols-1
       
        while l<=r:
            m=(l+r)//2
            i,j=m//cols,m%cols
            if matrix[i][j]>target:
                r=m-1
            elif matrix[i][j]<target:
                l=m+1
            else:
                return True
        return False
        
        #O(log(m*n))
        #O(1)
        #Index of mid to matrix -> i,j=m//cols,m%cols
        #Matrix indices to flatten arr index-> i,j->i*cols+j


        


        
        