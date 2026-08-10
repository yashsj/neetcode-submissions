class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        indegree=[0]*numCourses
        adj=[[] for i in range(numCourses)]
        for src,dest in prerequisites:
            indegree[src]+=1
            adj[dest].append(src)
        
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        courses=0
        while q:
            nie=q.popleft()
            courses+=1
            for c in adj[nie]:
                indegree[c]-=1
                if indegree[c]==0:
                    q.append(c)
            
        return courses==numCourses
        # TC:O(V+E) Khan's 
        # SC:O(V+E)


 