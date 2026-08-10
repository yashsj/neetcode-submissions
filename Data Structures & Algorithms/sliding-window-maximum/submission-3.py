class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        length=len(nums)
        if length <= k: 
            return [max(nums)]
        l,r=0,k-1
        ans=list()
        while l<length-k+1:
            slice_list=nums[l:r+1]
            max_elem=max(slice_list)
            ans.append(max_elem)
            l+=1
            r+=1
        return ans

