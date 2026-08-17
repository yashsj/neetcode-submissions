class Solution:
    def maximumProfit(self, profit: List[int], weight: List[int], capacity: int) -> int:
        N,M=len(weight),capacity
        dp=[[0]*(M+1) for _ in range(N)]

        """handle the edge cases, first making sure that we have a 0 in the first 
        column because because we can't really pick weight if only the available capacity is 0
        and then in the first row when we have access to the 1st item we can only pick it up if and only if matches the capacity if cap is lower than that we can never pick it up """
    
        for i in range(N):
            dp[i][0]=0
        for c in range(M+1):
            if weight[0]<=c:
                dp[0][c]=profit[0]

        for i in range(1,N):
            for c in range(1,M+1):
                skip=dp[i-1][c]
                include=0
                if c-weight[i]>=0:
                    include=profit[i]+dp[i-1][c-weight[i]]
                dp[i][c]=max(skip,include)
        return dp[N-1][M]


