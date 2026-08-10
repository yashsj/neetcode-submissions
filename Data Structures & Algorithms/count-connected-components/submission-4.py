class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        components=n
        parent=[i for i in range(n)]
        rank=[1]*n
        def find(n):
            if parent[n]!=n:
                parent[n]=find(parent[n])   
            return parent[n]

        def union(n1,n2):
            nonlocal components
            n1,n2=find(n1),find(n2)
            if n1==n2:
                return
            else:
                if rank[n1]>rank[n2]:
                    parent[n2]=n1    
                elif rank[n2]>rank[n1]:
                    parent[n1]=n2
                else:
                    parent[n2]=n1
                    rank[n1]+=1
                components-=1
            return
      

        for a,b in edges:
            union(a,b)
        return components
        