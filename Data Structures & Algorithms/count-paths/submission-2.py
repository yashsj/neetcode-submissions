class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        rows=m
        cols=n
        prev_row=[0]*cols
        for i in range(rows-1,-1,-1):
            curr_row=[0]*cols
            curr_row[cols-1]=1
            for j in range(cols-2,-1,-1):
                curr_row[j]=prev_row[j]+curr_row[j+1]
            prev_row=curr_row

        return curr_row[0]