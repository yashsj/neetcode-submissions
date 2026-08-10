class Solution:
    def findMin(self, nums: List[int]) -> int:
        l,r=0,len(nums)-1
        minv=float("inf")
        while(l<=r):
            if nums[l]<nums[r]:
                minv=min(minv,nums[l])
                break;
            m=(l+r)//2
            minv=min(minv,nums[m])
            if nums[l]<=nums[m]:
                l=m+1
            else:
                r=m-1
        return minv

        