class Solution:
    def minimumSpanningTree(self, n: int, edges: List[List[int]]) -> int:
        adj={}
        for i in range(n):
            adj[i]=[]
        for source,dest,weight in edges:
            adj[source].append([dest,weight])
            adj[dest].append([source,weight])
        minheap=[[0,0]]
        visited=set()
        ans=0
        while minheap and len(visited)<n:
            weight,node=heapq.heappop(minheap)
            if node in visited:
                continue 
            ans+=weight
            visited.add(node)
            
            for nei,wei in adj[node]:
                if nei not in visited:
                    heapq.heappush(minheap,[wei,nei])
        return ans if len(visited)==n else -1