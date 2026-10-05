class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum=sum(nums)
        if totalSum%2:
            return False
        target=totalSum//2
        hashset=set()
        hashset.add(0)
        for i in range(len(nums)):
            newset=set(hashset)
            for t in hashset:
                if target in newset:
                    return True
                newset.add(t+nums[i])
                newset.add(t)
            hashset=newset
        return False

            

        