class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """nums = [3,4,5,6,1,2], target = 1
        mid=left=0,right=5
        mid=5//2->2
        2==target? -> no!
        """


        left,right=0,len(nums)-1
        while left<=right:
            mid=(left+right)//2
            if nums[mid]==target:
                return mid 

            if nums[left]<=nums[mid]:
                if nums[left]<=target<nums[mid]:
                    right=mid-1
                else:
                    left=mid+1
            else:
                if nums[mid]<target<=nums[right]:
                    left=mid+1
                else:
                    right=mid-1
        return -1
            



            
