class TrieNode:
    def __init__(self):
        self.eow=False
        self.child={}

class WordDictionary:

    def __init__(self):
        self.root=TrieNode()
        

    def addWord(self, word: str) -> None:
        curr=self.root 
        for char in word:
            if char not in curr.child:
                curr.child[char]=TrieNode()
            curr=curr.child[char]
        curr.eow=True

        

    def search(self, word: str) -> bool:
        def dfs(j,root):
            curr=root
            for i in range(j,len(word)):
                char=word[i]
                if char==".":
                    for character in curr.child.values():
                        if dfs(i+1,character):
                            return True
                    return False

                else:
                    if char not in curr.child:
                        return False
                    curr=curr.child[char]
            return curr.eow
        return dfs(0,self.root)

            
        
