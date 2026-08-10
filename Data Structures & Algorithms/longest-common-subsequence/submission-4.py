class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Recursion
        # def dfs(i,j):
        #     if i==len(text1) or j==len(text2):
        #         return 0
            
        #     if text1[i]==text2[j]:
        #         return 1+dfs(i+1,j+1)

        #     return max(dfs(i+1,j),dfs(i,j+1))

        # return dfs(0,0)
        #TC: O(2^M+N)
        #SC: O(M+N)

        #DP Top down Memoization
        # N,M=len(text1),len(text2)
        # dp=[[-1]*(M) for _ in range(N)]

        # def dfs(i,j):
        #     if i==len(text1) or j==len(text2):
        #         return 0
        #     if dp[i][j]!=-1:
        #         return dp[i][j]
            
        #     if text1[i]==text2[j]:
        #         dp[i][j]= 1+dfs(i+1,j+1)
        #     else:
        #         dp[i][j]=max(dfs(i+1,j),dfs(i,j+1))

        #     return dp[i][j]

        # return dfs(0,0)

        #TC:O(M*N)
        #SC:O(M*N)

        #DP Bottom Up
        N,M=len(text1),len(text2)
        dp=[[-1]*(M+1) for _ in range(N+1)]
        for i in range(N+1):
            dp[i][0]=0
        for j in range(M+1):
            dp[0][j]=0
        
        for i in range(1,N+1):
            for j in range(1,M+1):
                if text1[i-1]==text2[j-1]:
                    dp[i][j]=1+dp[i-1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i-1][j])
        return dp[N][M]




        

        