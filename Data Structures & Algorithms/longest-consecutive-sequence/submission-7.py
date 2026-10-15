class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        ans=0
        hashset=set(nums)
        i=0
        j=len(nums)-1
        while i<=j:
            if nums[i]-1 not in hashset:
                value=1
                while nums[i]+value in hashset:
                    value+=1
                ans=max(ans,value)
            i+=1
        return ans

        #O(N)
        #O(N)
                

        