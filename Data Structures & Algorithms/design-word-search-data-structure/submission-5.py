class PrefixNode:
    def __init__(self):
        self.children={}
        self.endword=False

class WordDictionary: 
    def __init__(self):
        self.root=PrefixNode()
    
    def addWord(self,word):
        curr=self.root
        for c in word:
            if c not in curr.children:
                curr.children[c]=PrefixNode()
            curr=curr.children[c]
        curr.endword=True
    
    def search(self,word):
        # curr=self.root
        def dfs(i,root):
            curr=root
            for j in range(i,len(word)):
                c=word[j]
                if c=='.':
                    for node in curr.children.values():
                        if dfs(j+1,node):
                            return True
                    return False
                else:
                    if c not in curr.children:
                        return False
                    curr=curr.children[c]
            return curr.endword
        return dfs(0,self.root)


    