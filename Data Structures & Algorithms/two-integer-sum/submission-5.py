class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        """Brute force--> i=0 j=i+1 to n nums[i]+nums[j]==target [i,j]
                        i=1....
                        TC O(N2) 
        Target = 10. target-nums[i]=nums[j] 10-4 =5 [(4,0)]
                                            10-5=5.  [(4,0),(5,1)]
                                            10-6=4 return [0,2]
        """
        hashMap={} 
        for i,n in enumerate(nums):
            c=target-n
            if c in hashMap:
                return [hashMap[c],i]
            hashMap[n]=i
        return []


        # prevMap = {}  # val -> index

        # for i, n in enumerate(nums):
        #     diff = target - n
        #     if diff in prevMap:
        #         return [prevMap[diff], i]
        #     prevMap[n] = i




            
            

        