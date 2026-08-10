class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        if sum(nums)%2 !=0:
            return False
        target = (sum(nums))//2

        hashset=set()
        hashset.add(0)
        newset=set(hashset)
        for i in range(len(nums)-1,-1,-1):
            hashset=set(newset)
            for c in hashset:
                t=c+nums[i]
                if t==target:
                    return True
                newset.add(t)
            hashset=newset
        
        return False


        