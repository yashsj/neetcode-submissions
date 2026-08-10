class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if not n:
            return False
        if n==1 and not edges:
            return True
        hashmap={i:[] for i in range(n)}
        for src,dest in edges:
            hashmap[dest].append(src)
            hashmap[src].append(dest)
        visited=set()
        prev=-1
        def dfs(i,prev):
            if i in visited:
                return False
            if hashmap[i]==[]:
                return True
            visited.add(i)
            # prev=i
            for nie in hashmap[i]:
                if nie==prev:
                    continue
                else:
                    if not dfs(nie,i):
                        return False
            return True
        
        return dfs(0,prev) and n==len(visited)
        