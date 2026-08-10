class Solution:
    def shortestPath(self, n: int, edges: List[List[int]], src1: int) -> Dict[int, int]:
        adj={}
        for i in range(n):
            adj[i]=[]
        
        for src,dst,weight in edges:
            adj[src].append([dst,weight])

        ans={}
        minheap=[[0,src1]]
        while minheap:
            w1,n1=heapq.heappop(minheap)
            if n1 in ans:
                continue
            ans[n1]=w1

            for n2,w2 in adj[n1]:
                if n2 not in ans:
                    heapq.heappush(minheap,[w1+w2,n2])

        for i in range(n):
            if i not in ans:
                ans[i]=-1
        return ans   
                


            