class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        # directed weighted graph + minmum time to reach (Djkstra's)
       #1) adj matrix
    #    2)minheap
    #    3)visited==n

        adj=collections.defaultdict(list)
        for i in range(len(times)):
            s,e,t=times[i]
            adj[s].append((e,t))
        
        heap=[]
        heapq.heappush(heap,(0,k))
        visited=set()
        while heap:
            w1,n1=heapq.heappop(heap)
            visited.add(n1)
            if len(visited)==n:
                return w1
            for n2,w2 in adj[n1]:
                if n2 not in visited:
                    heapq.heappush(heap,(w1+w2,n2))
        return -1

