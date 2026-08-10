class TrieNode:
    def __init__(self):
        self.endOfword=False
        self.children={}

class PrefixTree:

    def __init__(self):
           self.root=TrieNode()
        

    def insert(self, word: str) -> None:
        curr=self.root
        for char in word:
            if char not in curr.children:
                curr.children[char]=TrieNode()
            curr=curr.children[char]
        curr.endOfword=True



    def search(self, word: str) -> bool:
        curr=self.root
        for char in word:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return curr.endOfword
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root 
        for char in prefix:
            if char not in curr.children:
                return False
            curr=curr.children[char]
        return True
        
        