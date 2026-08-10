class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        precourse={i: [] for i in range(numCourses)}
        for crs,pre in prerequisites:
            precourse[crs].append(pre)
        visited=set()
        def dfs(crs):
            if crs in visited:
                return False
            if precourse[crs]==[]:
                return True
            visited.add(crs)
            for n in precourse[crs]:
                if not dfs(n):
                    return False
                visited.remove(crs)
                precourse[n]=[]
                return True
            

        for c in range(numCourses):
            if not dfs(c):
                return False
        return True
        
         
        