class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0
        ROWS=len(grid)
        COLS=len(grid[0])
        islands=0
        visited=set()
        def bfs(row,col):
            queue=collections.deque()
            visited.add((row,col))
            queue.append((row,col))
            while queue:
                row,col=queue.popleft()
                directions=[[1,0],[-1,0],[0,-1],[0,1]]
                for dr,dc in directions:
                    rows,cols=row+dr,col+dc
                    if (rows) in range(ROWS) and (cols)in range(COLS) and grid[rows][cols]=="1" and ((rows,cols)) not in visited:
                        queue.append((rows,cols))
                        visited.add((rows,cols))


        for row in range(ROWS):
                for col in range(COLS):
                    if grid[row][col]=="1" and (row,col) not in visited:
                        bfs(row,col)
                        islands+=1
        return islands  




        