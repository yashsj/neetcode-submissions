class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        visited=set()
        path=set()
        topsort=[]
        adj={}
        for i in range(n):
            adj[i]=[]
        
        for src,dst in edges:
            adj[src].append(dst)
        
        def dfs(n):
            if n in path:
                return False
            if n in visited:
                return True 
            path.add(n)

            for nei in adj[n]:
                if not dfs(nei):
                    return False

            path.remove(n)
            visited.add(n)
            topsort.append(n)
            return True
                    
        for i in range(n):
            if not dfs(i):
                return []
        topsort.reverse()
        return topsort 