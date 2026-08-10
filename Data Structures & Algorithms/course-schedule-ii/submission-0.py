class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(numCourses)}
        indegree=[0]*numCourses
        for src,dest in prerequisites:
            adj[dest].append(src)
            indegree[src]+=1
        q=deque()
        for i in range(len(indegree)):
            if indegree[i]==0:
                q.append(i)
        result=[]
        while q:
            c=q.popleft()
            result.append(c)
            for l in adj[c]:
                indegree[l]-=1
                if indegree[l]==0:
                    q.append(l)
        
        return result if len(result)==numCourses else []


        