class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totSum=sum(nums)
        if totSum%2:
            return False
        target=totSum//2
        hashSet=set()
        hashSet.add(0)
        for i in range(len(nums)):
            newhash=set(hashSet)
            for t in hashSet:
                if target in newhash:
                    return True
                newhash.add(t+nums[i])
                newhash.add(t)
            hashSet=newhash
        return False

        
        