class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        #Q238->LC
        res=[1]*len(nums)
        prefix=1
        suffix=1
        for i in range(len(nums)):
            res[i]=prefix
            prefix=prefix*nums[i]
        
        for j in range(len(nums)-1,-1,-1):
            res[j]*=suffix
            suffix*=nums[j]
        return res




    
        