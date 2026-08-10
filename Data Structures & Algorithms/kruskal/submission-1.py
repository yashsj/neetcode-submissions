class UnionFind:
    def __init__(self,n:int):
        self.parent=[i for i in range(n)]
        self.rank=[1]*n

    def find_parent(self,n:int):
        if n!=self.parent[n]:
            self.parent[n]=self.find_parent(self.parent[n])
        return self.parent[n]
    
    def union(self,n1:int,n2:int):
        p1=self.find_parent(n1)
        p2=self.find_parent(n2)
        if p1!=p2:
            if self.rank[p1]<self.rank[p2]:
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
        for node1,node2,weight in edges:
            heapq.heappush(minheap,[weight,node1,node2])
        unionFind=UnionFind(n)
        res,components=0,n
        while components>1 and minheap:
            weight,node1,node2=heapq.heappop(minheap)
            if  unionFind.union(node1,node2):
                res+=weight
                components-=1

        return res if components==1 else -1

            
