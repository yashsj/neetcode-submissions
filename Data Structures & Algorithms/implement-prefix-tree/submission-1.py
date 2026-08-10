class TrieNode:
    def __init__(self):
        # self.key=''
        self.hashmap={}
        self.end=False

class PrefixTree:
    def __init__(self):
        self.root=TrieNode() 

    def insert(self, word: str) -> None:
        curr=self.root
        for c in word:
            if c not in curr.hashmap:
                node=TrieNode()
                curr.hashmap[c]=node
            curr=curr.hashmap[c]
        curr.end=True

    def search(self, word: str) -> bool:
        curr=self.root
        for c in word:
            if c not in curr.hashmap:
                return False
            curr=curr.hashmap[c]
        return curr.end
        

    def startsWith(self, prefix: str) -> bool:
        curr=self.root
        for c in prefix:
            if c not in curr.hashmap:
                return False
            curr=curr.hashmap[c]
            return True

        
        