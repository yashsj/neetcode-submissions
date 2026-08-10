class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        rows,cols=len(grid),len(grid[0])
        visited=set()
        area=0
        
        def bfs(row,col):
            queue=collections.deque()
            queue.append((row,col))
            directions=[[1,0],[0,1],[-1,0],[0,-1]]
            big=1
            while queue:
                new_row,new_col=queue.popleft()
                for dr,dc in directions:
                    new_rows,new_cols=new_row+dr,new_col+dc
                    if new_rows in range(rows) and  new_cols in range(cols) and grid[new_rows][new_cols]==1 and ((new_rows, new_cols)) not in visited:
                        queue.append((new_rows,new_cols))
                        visited.add((new_rows,new_cols))
                        big=big+1
            return big

        for row in range(rows):
            for col in range(cols):
                if grid[row][col]==1 and ((row,col)) not in visited:
                    visited.add((row,col))
                    area=max(bfs(row,col),area)
                    
        return area