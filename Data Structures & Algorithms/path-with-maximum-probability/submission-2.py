
class Solution:
    def maxProbability(self, n: int, edges: List[List[int]], succProb: List[float], start_node: int, end_node: int) -> float:
        adj=collections.defaultdict(list)
        for i in range(len(edges)):
            src,tar=edges[i]
            adj[src].append((tar,succProb[i]))
            adj[tar].append((src,succProb[i]))

        heap=[]
        heapq.heappush(heap,(-1,start_node))
        visited=set()
        # ans=float(1)

        while heap:
            w,n=heapq.heappop(heap)
            visited.add(n)
            if n == end_node:
                return w*-1
            for n1,w1 in adj[n]:
                if n1 not in visited:
                    heapq.heappush(heap,(float(w*w1),n1))
        return 0.0


                


        