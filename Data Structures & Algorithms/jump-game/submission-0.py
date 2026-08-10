class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal=len(nums)-1
        for i in range(len(nums)-1,-1,-1):
            count=nums[i]+i
            if count>=goal:
                goal=i

        return True if goal==0 else False
        