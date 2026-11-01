class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum=sum(nums)
        if totalSum%2:
            return False
        hashset=set()
        hashset.add(0)
        target=totalSum//2
        for i in range(len(nums)):
            newSet=set(hashset)
            for t in hashset:
                if target in newSet:
                    return True
                newSet.add(t+nums[i])
                newSet.add(t)
            hashset=newSet
        return False
            
        