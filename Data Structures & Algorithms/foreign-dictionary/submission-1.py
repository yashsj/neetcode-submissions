class Solution:
    def foreignDictionary(self, words: List[str]) -> str:
        adj={c:set() for word in words for c in word}
        indegree={c:0 for c in adj}
        queue=deque()
        ans=[]
        # for i in range(len(words)-1):
        #     w1,w2=words[i],words[i+1]
        #     l1=min(len(w1),len(w2))

        for i in range(len(words)-1):
            w1,w2=words[i],words[i+1]
            l1=min(len(w1),len(w2))
            if w1[:l1]==w2[:l1] and len(w1)>len(w2):
                return ""
            for j in range(l1):
                if w1[j]!=w2[j]:
                    setval=adj[w1[j]]
                    if w2[j] not in setval:
                        adj[w1[j]].add(w2[j])
                        indegree[w2[j]]+=1
                    break;
        for key,value in indegree.items():
            if value==0:
                queue.append(key)
        
        while queue:
            k=queue.popleft()
            ans.append(k)
            values=adj[k]
            for v in values:
                indegree[v]-=1
                if indegree[v]==0:
                    queue.append(v)
        
        if len(ans)!=len(adj):
            return ""
        return "".join(ans)



        
