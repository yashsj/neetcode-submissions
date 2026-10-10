class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        "[-4,-1,-1,0,1,2]"
        #sort it ->O(nlogn) + (n)
        nums.sort()
        res=[]
       
        for i in range(len(nums)):
            if nums[i]>0:
                break
            if i>=1 and nums[i]==nums[i-1]:
                continue
            left,right=i+1,len(nums)-1
            while left <right:
                ans=nums[i]+nums[left]+nums[right]
                if ans<0:
                    left+=1
                elif ans>0:
                    right-=1
                else:
                    res.append([nums[i],nums[left],nums[right]])
                    left+=1
                    right-=1
                    while nums[left]==nums[left-1] and left<right:
                        left+=1

        return res 


            
            


        