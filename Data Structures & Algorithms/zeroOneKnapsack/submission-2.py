class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        return self.dfs(0,profit,weight,capacity)
    
    def dfs(self,i,profit,weight,capacity):
        if i==len(profit):
            return 0

        #skip the current item i 
        maxProfit=self.dfs(i+1,profit,weight,capacity)


        #include the current item i 

        newcapacity=capacity-weight[i]
        if newcapacity>=0:
            p=profit[i]+self.dfs(i+1,profit,weight,newcapacity)
            maxProfit=max(p,maxProfit)
        return maxProfit