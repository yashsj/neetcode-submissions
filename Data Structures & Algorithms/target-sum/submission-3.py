class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #Recursion

        def dfs(i,nums,target,currsum):
            if i == len(nums):
                if currsum==target:
                    return 1
            if i>=len(nums):
                return 0
            
            ans = dfs(i+1,nums,target,currsum+nums[i]) + dfs(i+1,nums,target,currsum-nums[i])
            return ans
        
        return dfs(0,nums,target,0)