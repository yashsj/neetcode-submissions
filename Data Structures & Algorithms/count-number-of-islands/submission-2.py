class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        self.result=0
        self.row,self.col=len(grid),len(grid[0])
        def dfs(i:int,j:int):
            if i<0 or j<0 or i>=self.row or j>=self.col or grid[i][j]=='0':
                return
            grid[i][j]='0'
            dfs(i+1,j)
            dfs(i-1,j)
            dfs(i,j+1)
            dfs(i,j-1)
            return
        for i in range(self.row):
            for j in range(self.col):
                if grid[i][j]=='1':
                    dfs(i,j)
                    self.result+=1
        return self.result

        