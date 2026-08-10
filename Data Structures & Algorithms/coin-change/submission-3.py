class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        n=len(coins)
        memo={}
        def dfs(i,amt):
            if amt==0:
                return 0
            if i==n:
                return 1e9
            if (i,amt) in memo:
                return memo[(i,amt)]
            
            #skip
            memo[(i,amt)]=dfs(i+1,amt)
            # include
            if amt-coins[i]>=0:
                count=1+dfs(i,amt-coins[i])
                memo[(i,amt)]=min(memo[(i,amt)],count)
            return memo[(i,amt)]
        result=dfs(0,amount)
        return -1 if result>=1e9 else result

