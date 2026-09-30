class Solution:
    def canPartition(self, nums: list[int]) -> bool:
        totalSum=sum(nums)
        target=totalSum//2
        if totalSum%2:
            return False
        dp=set()
        dp.add(0)
        for i in range(len(nums)):
            nextDP=set(dp)
            for t in dp:
                if target in nextDP:
                    return True
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp=nextDP
        return False
        