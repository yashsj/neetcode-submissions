class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        M,N=len(weight),capacity
        cache=[[-1]*(N+1) for _ in range(M)]
        return self.memo(0,profit,weight,capacity,cache)

    def memo(self,i,profit,weight,capacity,cache):
        if i==len(weight):
            return 0
        
        if cache[i][capacity]!=-1:
            return cache[i][capacity]
        
        #skip
        cache[i][capacity]=self.memo(i+1,profit,weight,capacity,cache)
        
        #include 
        newCap=capacity-weight[i]
        if newCap>=0:
            p=profit[i]+self.memo(i+1,profit,weight,newCap,cache)
            cache[i][capacity]=max(p,cache[i][capacity])
        return cache[i][capacity]

