class UnionFind:
    def __init__(self,n):
        self.parent=[i for i in range(n)]
        self.rank=[1]*n
        
    def find(self,n):
        while self.parent[n]!=n:
            self.parent[n]=self.parent[self.parent[n]]
            n=self.parent[n]
        return n

    def union(self,n1,n2):
        p1,p2=self.find(n1),self.find(n2)
        if p1==p2:
            return False
        
        # if self.rank[p1]<self.rank[p2]:
        #     self.parent[p1]=p2
        # elif self.rank[p1]>self.rank[p2]:
        #     self.parent[p2]=p1
        # else:
        #     self.parent[p1]=p2
        #     self.rank[p2]+=1

    #*** rank = size of the component (number of nodes)
        if self.rank[p1] > self.rank[p2]:
            self.parent[p2] = p1
            self.rank[p1] += self.rank[p2]
        else:
            self.parent[p1] = p2
            self.rank[p2] += self.rank[p1]
        return True

        
class Solution:
    def findCriticalAndPseudoCriticalEdges(self, n: int, edges: List[List[int]]) -> List[List[int]]:

        for i,e in enumerate(edges):
            e.append(i)
        
        edges.sort(key=lambda e:e[2])
        
        uf=UnionFind(n)
        min_weight=0
        for s,t,w,p in edges:
            if not uf.union(s,t):
                continue
            min_weight+=w
        
        critical,pseudo=[],[]
        # uf=UnionFind(n)
        for s,t,w,p in edges:
            uf=UnionFind(n)
            weight=0
            for s1,t1,w1,p1 in edges:
                if p==p1:
                    continue
                if uf.union(s1,t1):
                    weight+=w1
            if max(uf.rank)!=n or weight>min_weight:
                critical.append(p)
                continue
            uf=UnionFind(n)
            uf.union(s,t)
            weight1=w
            for s1,t1,w1,p1 in edges:
                if uf.union(s1,t1):
                    weight1+=w1
            if weight1==min_weight:
                pseudo.append(p)
        return [critical,pseudo]
                

            
            
            

            





        









