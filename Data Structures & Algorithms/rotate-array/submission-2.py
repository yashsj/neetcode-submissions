class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        l,r=0,n-1
        def reverse_list(nums,l,r)->None:
            while l<r:
                nums[l],nums[r]=nums[r],nums[l]
                l+=1
                r-=1
        
        reverse_list(nums,l,r)
        reverse_list(nums,l,k-1)
        reverse_list(nums,k,r)
    

        