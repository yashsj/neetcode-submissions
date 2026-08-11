class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M=len(profit),capacity
        cache=[[-1]*(M+1) for _ in range(N)]
        return self.dfs(0,profit,weight,capacity,cache)
    
    def dfs(self,i,profit,weight,capacity,cache):
        if i==len(weight):
            return 0
        if cache[i][capacity]!=-1:
            return cache[i][capacity]
        
        #skip the ith item
        res = self.dfs(i+1,profit,weight,capacity,cache)
        
        #include
        newCap=capacity-weight[i]
        if newCap>=0:
            p=profit[i]+self.dfs(i+1,profit,weight,newCap,cache)
            res = max(p, res)
        
        cache[i][capacity] = res
        return cache[i][capacity]
