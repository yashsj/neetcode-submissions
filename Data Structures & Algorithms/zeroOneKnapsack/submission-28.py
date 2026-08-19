class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M=len(weight),capacity
        cache=[[-1]*(M+1) for _ in range(N)]
        return self.ans(0,profit,weight,capacity,cache)


    def ans(self,i,profit,weight,capacity,cache): 
        if i==len(weight):
            return 0 

        if cache[i][capacity]!=-1:
            return cache[i][capacity]

        #skip
        cache[i][capacity]=self.ans(i+1,profit,weight,capacity,cache)

        #include
        newCap=capacity-weight[i]
        if newCap>=0:
            p=profit[i]+self.ans(i+1,profit,weight,newCap,cache)
            cache[i][capacity]=max(cache[i][capacity],p)
        return cache[i][capacity]
        

