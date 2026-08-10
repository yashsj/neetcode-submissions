class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        n=len(coins)
        dp={}
        def dfs(i,amt):
            if i>=n or amt<0:
                return 0
            if amt==0:
                return 1
            if (i,amt) in dp:
                return dp[(i,amt)]
            res=dfs(i+1,amt)
            if amt>=coins[i]:
                res+=dfs(i,amt-coins[i])
            dp[(i,amt)]=res
            return res
        
        return dfs(0,amount)
        