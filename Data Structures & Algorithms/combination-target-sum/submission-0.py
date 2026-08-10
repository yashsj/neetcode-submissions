class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        res,sol=[],[]
        n=len(nums)
        def dfs(i,cur_sum):
            if cur_sum==target:
                res.append(sol[:])
                return 
            if n==i or cur_sum>target:
                return 
            
            dfs(i+1,cur_sum)

            sol.append(nums[i])
            dfs(i,cur_sum+nums[i])
            sol.pop()
        dfs(0,0)
        return res