class UnionFind:
    def __init__(self,n:int):
        self.parent=[i for i in range (n)]
        self.rank=[1]*n
    
    def find(self,n)->int:
        if self.parent[n]!=n:
            self.parent[n]=self.find(self.parent[n])
        return self.parent[n]
    
    def union(self,node1:int,node2:int)->bool:
        p1,p2=self.find(node1),self.find(node2)
        if p1!=p2:
            if self.rank[p1]>self.rank[p2]:
                self.parent[p1]=p2
                self.rank[p2]+=self.rank[p1]
            else:
                self.parent[p2]=p1
                self.rank[p1]+=self.rank[p2]
            return True
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minheap=[]
        for n1,n2,weight in edges:
            heapq.heappush(minheap,[weight,n1,n2])
        unionfind=UnionFind(n)
        res,components=0,n

        while components>1 and minheap:
            weight,n1,n2 =heapq.heappop(minheap)
            if unionfind.union(n1,n2):
                res+=weight
                components-=1
        return res if components==1 else -1
        
