class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        
        curr_sum=0
        i=j=0
        n=len(nums)
        min_val=n+1
        while(j<n and i<=j):
            curr_sum+=nums[j]
            while i<=j and curr_sum>=target:
                min_val=min(min_val,j-i+1)
                curr_sum-=nums[i]
                i+=1
            j+=1
        return min_val if min_val != n+1 else 0
