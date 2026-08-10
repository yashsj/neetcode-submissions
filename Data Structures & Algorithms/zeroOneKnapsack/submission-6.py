class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M=len(weight),capacity
        memo=[[-1] *(M+1) for _ in range(N)]
        return self.memoization(0,profit,weight,capacity,memo)
    
    def memoization(self,i,profit,weight,capacity,memo)-> int:
        if i==len(weight):
            return 0
        
        #Exclude 
        if memo[i][capacity]!=-1:
            return memo[i][capacity]
        memo[i][capacity]= self.memoization(i+1,profit,weight,capacity,memo)
        

        #include the next item
        newCap=capacity-weight[i]
        if newCap>=0:
            take=profit[i]+self.memoization(i+1,profit,weight,newCap,memo)
            memo[i][capacity]=max(memo[i][capacity],take)
        return memo[i][capacity]