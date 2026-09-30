class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum=sum(nums)
        if totalSum%2==1:
            return False
        target=totalSum//2
        dp=set()
        dp.add(0)
        for i in range(len(nums)):
            nextDP=set(dp)
            for t in dp:
                if (t+nums[i])==target:
                    return True
                nextDP.add(t+nums[i])
                nextDP.add(t)
            dp=nextDP
        return False


        