class UnionFind:
    def __init__(self,x:int):
        self.rank=[1]*n
        self.parent=[i for i in range(n)]
    
    def find(self,x:int):
        if x!=self.parent[x]:
            self.parent[x]=self.find(self.parent[x])
        return self.parent[x]
    
    def union(self,node1:int,node2:int):
        p1,p2=self.find(node1),self.find(node2)
        if p1!=p2:
            if self.rank[p1]>self.rank[p2]:
                self.parent[p2]=p1
                self.rank[p1]+=self.rank[p2]
            else:
                self.parent[p1]=p2
                self.rank[p2]+=self.rank[p1]
            return True
        return False

class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        minheap=[]
        ans=0
        components=n
        unionfind=UnionFind(n)
        for n1,n2,weight in edges:
            heapq.heappush(minheap,[weight,n1,n2])
        while components>=1 and minheap:
            weight,n1,n2=heapq.heappop(minheap)
            if unionfind.union(n1,n2):
                ans+=weight
                components-=1
        return ans if components==1 else -1
            
