class Solution:
    def shortestPath(self, grid: List[List[int]]) -> int:
        ROW,COL=len(grid),len(grid[0])
        visited=set()
        count=0
        visited.add((0,0))
        queue=collections.deque()
        queue.append((0,0))
        while queue:
            for i in range(len(queue)):
                new_r,new_c=queue.popleft() 
                if new_r==ROW-1 and new_c==COL-1:
                    return count

                directions=[[1,0],[0,1],[-1,0],[0,-1]]  
                for dr,dc in directions:
                    new_row,new_col=new_r+dr,new_c+dc
                    if(new_row<0 or new_col<0 or new_row==ROW or new_col==COL or grid[new_row][new_col]==1 or ((new_row,new_col) in visited)):
                        continue
                    queue.append((new_row,new_col))
                    visited.add((new_row,new_col))
            count=count+1
        return -1
    


        