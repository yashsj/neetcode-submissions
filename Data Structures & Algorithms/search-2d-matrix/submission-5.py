class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        up=0
        down=len(matrix)-1
        left,right=0,len(matrix[0])-1
        range_list=0
        while(up<=down):
            mid=(up+down)//2
            if matrix[mid][left]<=target<=matrix[mid][right]:
                range_list=mid
                break;
            elif matrix[mid][left]<target and matrix[mid][right] < target:
                up=mid+1
            else:
                down=mid-1
        left=0
        right=len(matrix[0])-1
        while(left<=right):
            mid=(left+right)//2
            if matrix[range_list][mid]==target:
                return True
            elif matrix[range_list][mid]<target:
                left=mid+1
            else:
                right=mid-1
        return False
        
            
