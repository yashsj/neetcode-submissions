class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows=m
        cols=n
        memo=[[-1]* cols for _ in range(rows)]
        def dfs(r,c):
            if r==rows or c==cols:
                return 0
            if r==rows-1 and c==cols-1:
                return 1 
            if memo[r][c]!=-1:
                return memo[r][c]
            
            memo[r][c]=dfs(r,c+1)+dfs(r+1,c)
            return memo[r][c]
        
        return dfs(0,0)

        