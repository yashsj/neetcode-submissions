class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfs(0,profit,weight,capacity)
    
    def dfs(self,i,profit,weight,capacity):
        if i==len(profit):
            return 0
        #skip that element 
        maxProfit=self.dfs(i+1,profit,weight,capacity)

        #include the element
        newCapacity=capacity-weight[i]
        if newCapacity>=0:
            p=profit[i]+self.dfs(i+1,profit,weight,newCapacity)
            maxProfit=max(maxProfit,p)
        return maxProfit
        
            

