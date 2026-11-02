class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        #[1,2,3,2,2]->dup,count=0,0
        #count->1,dup=1 ,count=0,dup=0
        #count->1,dup=3
        #count->0,dup=0
        #count->1,dup=2
        #count->

        for n in nums:
            idx=abs(n)-1
            if nums[idx]<0:
                return abs(n)
            nums[idx]*=-1

        #Modifying the input array
        #TC O(N)
        #SC O(1)

        #Not modifying will go with Floyd's cycle detection algo

        
        