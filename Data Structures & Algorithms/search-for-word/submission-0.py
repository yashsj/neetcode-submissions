class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        self.row=len(board)
        self.col=len(board[0])
        def dfs(i,j,index):
            if index==len(word):
                return True
            if i<0 or j<0 or i>=self.row or j>=self.col or board[i][j]!=word[index]:
                return False
            board[i][j]='#'
            res = dfs(i+1,j,index+1) or dfs(i-1,j,index+1) or dfs(i,j+1,index+1) or dfs(i,j-1,index+1)
            board[i][j]=word[index]
            return res

        for i in range(self.row):
            for j in range(self.col):
                if board[i][j]==word[0]:
                    if dfs(i,j,0):
                        return True
        return False
                

        
        