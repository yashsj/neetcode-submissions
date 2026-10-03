class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum=sum(nums)
        if totalSum%2:
            return False
        target=totalSum//2
        hashset=set()
        hashset.add(0)
        for i in range(len(nums)):
            newHash=set(hashset)
            for t in hashset:
                if target in newHash:
                    return True
                newHash.add(t+nums[i])
                newHash.add(t)
            hashset=newHash
        return False
                

        