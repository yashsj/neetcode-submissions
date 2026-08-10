class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        row=m
        col=n

        def dfs(r,c):
            if r==row or c==col:
                return 0
            if r==row-1 and c==col-1:
                return 1
            
            return dfs(r+1,c) +dfs(r,c+1)
            
        return dfs(0,0)
            
        