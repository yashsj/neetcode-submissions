class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        #bottom up dp programming
        dp=[0]*(len(days)+1)
        
        for i in reversed(range(len(days))):
            dp[i]=float('inf')
            j=i
            for cost,duration in zip(costs,[1,7,30]):
                while j<len(days) and days[j]<days[i]+duration:
                    j+=1
                dp[i]=min(dp[i],cost+dp[j])

        return dp[0]



        