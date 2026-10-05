class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hashMap={}
        for i,n in enumerate(nums):
            c=target-n
            if c in hashMap:
                return [hashMap[c],i]
            hashMap[n]=i
        return []
            


        