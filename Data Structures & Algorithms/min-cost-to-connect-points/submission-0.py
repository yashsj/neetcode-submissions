class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        #minimum spanning tree(Prims)- acyclic , undirected, connected graph 
        #Connect all the nodes such that minimum cost to connect all points
        #Note :- V vertices E=V-1 edges
        adj=collections.defaultdict(list)
        N=len(points)
        for i in range(N):
            for j in range(i+1,N):
                x1,y1=points[i]
                x2,y2=points[j]
                dist=abs(x1-x2)+abs(y1-y2)
                adj[i].append((j,dist))
                adj[j].append((i,dist))

            heap=[]
            heapq.heappush(heap,(0,0))
            cost=0
            visited=set()
            while len(visited)<N:
                d1,v1=heapq.heappop(heap)
                if v1 in visited:
                    continue
                cost+=d1
                visited.add(v1)
                for v2,d2 in adj[v1]:
                    if v2 not in visited:
                        heapq.heappush(heap,(d2,v2))
        return cost






        
            
        