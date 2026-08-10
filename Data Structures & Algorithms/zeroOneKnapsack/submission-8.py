class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        
        return self.dfs(0,profit,weight,capacity)
    
    def dfs(self,i,profit,weight,capacity):
        ans=0
        if i==len(weight):
            return 0
        
        #exclude the item
        ans=self.dfs(i+1,profit,weight,capacity)
        #include the item 
        newCap=capacity-weight[i]
        if newCap>=0:
            p=profit[i]+self.dfs(i+1,profit,weight,newCap)
            ans=max(ans,p)
        return ans 
