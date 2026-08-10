class TrieNode:
    def __init__(self):
        self.hashmap={}
        self.endofword=False
class Solution:
    def __init__(self):
        self.root=TrieNode()
        # self.row=len(board)
        # self.col=len(board[0])
        # self.ans=[]

    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        ans=set()
        row=len(board)
        col=len(board[0])
        for w in words:
            curr=self.root
            for c in w:
                if c not in curr.hashmap:
                    curr.hashmap[c]=TrieNode()
                curr=curr.hashmap[c]
            curr.endofword=True
        
        def dfs(i,j,curr,temp):
            if i<0 or j<0 or i>=row or j>=col:
                return
            if board[i][j] not in curr.hashmap or board[i][j] == '#':
                return
            temp.append(board[i][j])
            curr=curr.hashmap[board[i][j]]
            c=board[i][j]
            board[i][j]='#'
            if curr.endofword== True:
                ans.add(''.join(temp))
            
            dfs(i+1,j,curr,temp)
            dfs(i-1,j,curr,temp)
            dfs(i,j+1,curr,temp)
            dfs(i,j-1,curr,temp)
            board[i][j]=c
            temp.pop()
            return
            

        for i in range(row):
            for j in range(col):
                if board[i][j] in self.root.hashmap:
                    dfs(i,j,self.root,[])
        return list(ans)

        