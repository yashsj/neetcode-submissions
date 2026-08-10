class Solution:
    def countPaths(self, grid: List[List[int]]) -> int:
        visited=set()
        ROWS,COLS=len(grid),len(grid[0])
        
        def helper(grid:List[List[int]],row:int,col:int,visit:set)->int:
                if min(row,col)<0 or row==ROWS or col==COLS or grid[row][col]==1 or (row,col) in visited:
                    return 0
                if row==ROWS-1 and col==COLS-1:
                    return 1
                visited.add((row,col))
                
                    
                    
                count=0
                count+=helper(grid,row+1,col,visited)
                count+=helper(grid,row,col+1,visited)
                count+=helper(grid,row-1,col,visited)
                count+=helper(grid,row,col-1,visited)
                visited.remove((row,col))
                return (count)

        return helper(grid,0,0,set())




        


                


