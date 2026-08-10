class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #Recursion

        def dfs(i,nums,target,currsum,ans):
            if i == len(nums):
                if currsum==target:
                    ans+=1
                    return ans
            if i>=len(nums):
                return 0
            
            ans = dfs(i+1,nums,target,currsum+nums[i],ans) + dfs(i+1,nums,target,currsum-nums[i],ans)
            return ans

        
        return dfs(0,nums,target,0,0)