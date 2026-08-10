class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M,N=capacity,len(weight)
        cache=[[-1]*(M+1) for _ in range(N)]
        return self.dfs(0,profit,weight,capacity,cache)
    
    def dfs(self,i,profit,weight,capacity,cache):
        if i==len(weight):
            return 0
        if cache[i][capacity]!=-1:
            return cache[i][capacity]

        #exclude the element at that pos
        cache[i][capacity]=self.dfs(i+1,profit,weight,capacity,cache)

        #including the element at that position
        newCap=capacity-weight[i]
        if newCap>=0:
            p=profit[i]+self.dfs(i+1,profit,weight,newCap,cache)
            cache[i][capacity]=max(p,cache[i][capacity])
        return cache[i][capacity]
        


        
