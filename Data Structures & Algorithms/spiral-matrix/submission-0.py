class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        top=0
        bottom=len(matrix)
        left=0
        right=len(matrix[0])
        size=len(matrix)*len(matrix[0])
        ans=[]
        while len(ans)!=size:
            for i in range(left,right):
                if len(ans)!=size:
                    ans.append(matrix[top][i])
            top+=1
            for i in range(top,bottom):
                if len(ans)!=size:
                    ans.append(matrix[i][right-1])
            right-=1
            for i in range(right-1,left-1,-1):
                if len(ans)!=size:
                    ans.append(matrix[bottom-1][i])
            bottom-=1
            for i in range(bottom-1,top-1,-1):
                if len(ans)!=size:
                    ans.append(matrix[i][left])
            left+=1
        return ans
        #TC:O(M*N)
        #SC:O(1)+O(M*N)