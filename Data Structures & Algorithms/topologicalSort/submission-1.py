class Solution:
    def topologicalSort(self, n: int, edges: List[List[int]]) -> List[int]:
        topsort=[]
        adj={}
        for i in range(n):
            adj[i]=[]
        for src,dest, in edges:
            adj[src].append(dest)
        visited=set()
        path=set()

        def dfs(src:int)->bool:
            if src in visited:
                return True
            if src in path:
                return False
            path.add(src)

            for n in adj[src]:
                if not dfs(n):
                    return False

            path.remove(src)
            visited.add(src)
            topsort.append(src)
            return True

        for i in range(n):
            if not dfs(i):
                return []
        topsort.reverse()
        return topsort 
